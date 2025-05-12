
import numpy as np
import gzip
import os
from astropy.io import fits

# List of input FITS files
fits_files = [
    "COM_CMB_IQU-smica_2048_R3.00_oe1.fits",
    "COM_CMB_IQU-smica_2048_R3.00_oe2.fits",
    "COM_CMB_IQU-smica_2048_R3.00_hm1.fits",
    "COM_CMB_IQU-smica_2048_R3.00_hm2.fits"
]

def normalize_to_255(arr):
    arr_min, arr_max = np.min(arr), np.max(arr)
    return ((arr - arr_min) / (arr_max - arr_min) * 255).astype(np.uint8)

def compression_ratio(file_path):
    original_size = os.path.getsize(file_path)
    compressed_path = file_path + ".gz"
    with open(file_path, 'rb') as f_in, gzip.open(compressed_path, 'wb') as f_out:
        f_out.writelines(f_in)
    compressed_size = os.path.getsize(compressed_path)
    return compressed_size / original_size

results = []

for file in fits_files:
    try:
        hdul = fits.open(file)
        cmb_data = hdul[1].data
        cmb_I = np.nan_to_num(cmb_data['I_STOKES'])
        cmb_array = cmb_I.flatten()

        # Normalize and save real map
        scaled = normalize_to_255(cmb_array)
        real_bin = file.replace(".fits", "_real.bin")
        with open(real_bin, "wb") as f:
            f.write(scaled.tobytes())

        # Create and save mock
        mock = np.random.normal(loc=np.mean(cmb_array), scale=np.std(cmb_array), size=cmb_array.shape)
        mock_scaled = normalize_to_255(mock)
        mock_bin = file.replace(".fits", "_mock.bin")
        with open(mock_bin, "wb") as f:
            f.write(mock_scaled.tobytes())

        # Run compression comparison
        real_ratio = compression_ratio(real_bin)
        mock_ratio = compression_ratio(mock_bin)
        bias = mock_ratio - real_ratio

        results.append((file, real_ratio, mock_ratio, bias))

        print(f"✔ {file}")
        print(f"  CMB Compression Ratio:       {real_ratio:.5f}")
        print(f"  Gaussian Noise Ratio:        {mock_ratio:.5f}")
        print(f"  Compression Advantage (bias): {bias:.5f}\n")

    except Exception as e:
        print(f"⚠ Failed on {file}: {e}")

# Summary table
print("\n=== Summary ===")
for file, real_ratio, mock_ratio, bias in results:
    print(f"{file}: CMB={real_ratio:.5f}, Mock={mock_ratio:.5f}, Bias={bias:.5f}")

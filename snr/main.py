import os
from typing import List, Tuple

import numpy as np
import pydicom


def get_dicom_files(path_input_folder: str) -> List[str]:
    """
    Find all DICOM files in the given folder.

    Parameters
    ----------
    path_input_folder : str
        Path to the directory containing DICOM files.

    Returns
    -------
    List[str]
        List of DICOM files.
    """
    if not os.path.exists(path_input_folder):
        raise FileNotFoundError(f"Folder '{path_input_folder}' does not exist.")

    dicom_files = [
        os.path.normpath(os.path.join(root, file))
        for root, _, files in os.walk(path_input_folder)
        for file in files
        if file.lower().endswith(".dcm")
    ]

    if not dicom_files:
        raise FileNotFoundError(
            f"No DICOM files (.dcm) found in '{path_input_folder}'."
        )
    return dicom_files


def create_dicom_3d_image(
    list_input_dicom: List[str], img_dims: Tuple[int, int, int], img_dtype: np.dtype
) -> np.ndarray:
    """
    Create a 3D image from a list of sorted DICOM slices.

    Parameters
    ----------
    list_input_dicom : List[str]
        Sorted list of DICOM file paths.
    img_dims : Tuple[int, int, int]
        Dimensions of the 3D image.
    img_dtype : np.dtype
        Data type of the pixel array.

    Returns
    -------
    np.ndarray
        3D NumPy array containing the pixel data.
    """
    array_dicom = np.zeros(img_dims, dtype=img_dtype)

    for dicom_path in list_input_dicom:

        ds = pydicom.dcmread(dicom_path)
        # Check the instance number, the size and the scale of the slice
        instance_number = getattr(ds, "InstanceNumber", None)
        rows_number = getattr(ds, "Rows", None)
        columns_number = getattr(ds, "Columns", None)
        photometric_interpretation = getattr(ds, "PhotometricInterpretation", None)
        image_array = ds.pixel_array

        assert instance_number, f"Missing InstanceNumber in file {dicom_path}."

        assert (
            rows_number == img_dims[2] or columns_number == img_dims[3]
        ), f"File {dicom_path}: dimensions do not match ({rows_number}x{columns_number} vs {img_dims[1]}x{img_dims[2]})."

        assert image_array.ndim == 2, f"File {dicom_path} is not 2D."

        assert (
            photometric_interpretation.upper() == "MONOCHROME1"
            or photometric_interpretation.upper() == "MONOCHROME2"
        ), f"File {dicom_path} is not monochrome."

        # Create the 3D image
        index = int(instance_number) - 1
        array_dicom[index, :, :] = image_array

    return array_dicom


def calculate_snr(image: np.ndarray, kernel_size: int) -> float:
    """
    Calculate the volume signal to noise ratio.

    Parameters
    ----------
    image : np.ndarray
        ArrayNumPy.
    kernel_size : int
        Dimensions of the kernel.

    Returns
    -------
    float
        SNR value.
    """
    C, H, W = image.shape

    # Background ROI
    roi_backgorund = image[:, :kernel_size, :kernel_size]

    # Object ROI
    center_h_start = (H - kernel_size) // 2
    center_w_start = (W - kernel_size) // 2
    roi_object = image[
        :,
        center_h_start : center_h_start + kernel_size,
        center_w_start : center_w_start + kernel_size,
    ]

    # Calculate SNR
    assert roi_backgorund.std() != 0, "Background standard deviation is zero."
    snr = roi_object.mean() / roi_backgorund.std()

    return float(round(snr, 2))


def save_snr_txt(
    snr: float,
    path_output_folder: str,
    series_number: str,
    format: str,
) -> bool:
    """
    Save the SNR value in the output folder as a text file.

    Parameters
    ----------
    snr : float
        SNR value.
    path_output_folder : str
        Folder where to save the text file
    series_num : str
        Series number
    format : str
        Format of the file

    Returns
    -------
    bool
        True if the SNR was saved correctly
    """
    if not os.path.exists(path_output_folder):
        raise FileNotFoundError(f"Folder '{path_output_folder}' does not exist.")

    output_path = os.path.join(path_output_folder, f"snr_scan_{series_number}.{format}")

    with open(output_path, "w") as file:
        file.write(f"SNR for scan {series_number}: {snr}")
    return True


def main():
    """
    Main function to process DICOM files, generate a 3D image, and save a histogram.
    """
    path_input_folder = "./input"
    path_output_folder = "./output"

    # Get a list of dicom files contained in XNAT input folder
    try:
        list_input_dicom = get_dicom_files(path_input_folder)
        print(
            f"Found {len(list_input_dicom)} DICOM files in '{path_input_folder}':\n"
            + "\n".join(f"'{file}'" for file in list_input_dicom)
        )
    except FileNotFoundError:
        raise
    except Exception as e:
        print(f"Error getting DICOM files: {e}")
        raise

    # Create a 3D image from a list of sorted (by InstanceNumber) DICOM slices.
    try:
        # Ensure DICOM files are sorted by InstanceNumber
        # get image dimensions and data type from the first DICOM file.
        list_input_dicom.sort(key=lambda x: pydicom.dcmread(x).InstanceNumber)

        print(
            "DICOM files sorted by InstanceNumber:\n"
            + "\n".join(f"'{file}'" for file in list_input_dicom)
        )

        ref_ds = pydicom.dcmread(list_input_dicom[0])

        img_dims = (len(list_input_dicom), int(ref_ds.Rows), int(ref_ds.Columns))
        img_dtype = ref_ds.pixel_array.dtype

        image_input_dicom = create_dicom_3d_image(list_input_dicom, img_dims, img_dtype)
        print(
            f"Successfully created 3D DICOM image with shape {image_input_dicom.shape}."
        )
    except AssertionError:
        raise
    except Exception as e:
        print(f"Error constructing 3D DICOM image: {e}")
        raise

    # Calculate SNR
    try:
        kernel_size = 5
        snr = calculate_snr(image_input_dicom, kernel_size)
    except Exception as e:
        print(f"Error calculating SNR {series_number}: {e}")
        raise

    # Save SNR in XNAT output folder
    try:
        # Get series number
        series_number = str(getattr(ref_ds, "SeriesNumber", "unknown"))
        save_snr_txt(snr, path_output_folder, series_number, "txt")
        print(f"SNR for scan {series_number} saved successfully.")
    except FileNotFoundError:
        raise
    except Exception as e:
        print(f"Error saving SNR for scan {series_number}: {e}")
        raise


if __name__ == "__main__":
    main()

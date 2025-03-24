# Docker-EOSC4Cancer-D2-2

## Prerequisites
Before starting, make sure you have installed:  
- [Docker](https://www.docker.com/)  

## Usage
Follow these steps to build and run the Docker container:

### 1. **Clone the repository**
   ```sh
   git clone https://github.com/FGammaraccio/Docker-EOSC4Cancer-D2-2.git
   ```

### 2. **Navigate to the project directory**
   ```sh
   cd Docker-EOSC4Cancer-D2-2
   ```

### 3. **Build the Docker image**
   **SNR**  
   The following command creates a Docker image named `snr` using the `Dockerfile` in the `snr` folder:
   ```sh
   docker build -t snr ./snr
   ```
   **Convolution 2D**    
   The following command creates a Docker image named `convolution_2d` using the `Dockerfile` in the `convolution_2d` folder:
   ```sh
   docker build -t convolution_2d ./convolution_2d
   ```

### 4. **Run the container**
### On Windows (CMD)
   **SNR Container**  
   ```sh
   docker run --rm ^
   -v "%cd%\data\input\03-18-1995-NA-ECT008IV---CT-ABDOMEN-W-CO-59531\SCANS\2\DICOM:/input" ^
   -v "%cd%\data\output\output_snr:/output" ^
   snr
   ```
   **Convolution 2D Container**  
   ```sh
   docker run --rm ^
   -v "%cd%\data\input\03-18-1995-NA-ECT008IV---CT-ABDOMEN-W-CO-59531\SCANS\2\DICOM:/input" ^
   -v "%cd%\data\output\output_convolution_2d:/output" ^
   convolution_2d
   ```
### On Unix-based Systems (Linux/macOS)
   **SNR Container**  
   ```sh
   docker run --rm \
   -v "$(pwd)/data/input/03-18-1995-NA-ECT008IV---CT-ABDOMEN-W-CO-59531/SCANS/2/DICOM:/input" \
   -v "$(pwd)/data/output/output_snr:/output" \
   snr
   ```
   **Convolution 2D Container**  
   ```sh
   docker run --rm \
   -v "$(pwd)/data/input/03-18-1995-NA-ECT008IV---CT-ABDOMEN-W-CO-59531/SCANS/2/DICOM:/input" \
   -v "$(pwd)/data/output/output_convolution_2d:/output" \
   convolution_2d
   ```
   **Bind mounts**  
   The docker run command uses the -v flag to mount a file or directory on the host machine from the host into a container:
   ```sh
   docker run -v <host-path>:<container-path>[:opts]
   ```
   where:  
        1. host-path: The location of the file or directory on the host. This can be an absolute or relative path.  
        2. container-path: The path where the file or directory is mounted in the container. Must be an absolute path.  
   [Documentation](https://docs.docker.com/engine/storage/bind-mounts/)


---

## Data

### Input
The input consists of a single patient's CT scan in DICOM format.  
Example dataset: [CT scan](https://xnat.health-ri.nl/app/action/DisplayItemAction/search_element/xnat%3ActSessionData/search_field/xnat%3ActSessionData.ID/search_value/BMIAXNAT_E87500/popup/false/project/eosc4cancer_tcga_coad)

### Output
- **SNR Output**: A text file containing the computed SNR.
- **Convolution 2D Output**: Filtered DICOM images and updated tags.

---

## About SNR 
**SNR** is a tool designed to calculate the Signal-to-Noise Ratio (SNR). It performs the following steps:

1. **Reads DICOM files** from the specified input folder.
2. **Constructs a 3D volume** by ordering the slices based on the DICOM Instance Number tag.
3. **Computes the SNR** in the 3D volume.
4. **Saves the SNR value** to a text file in the output folder.

## About Convolution 2D
**2D Convolution** is a tool designed to perform 2D convolution (image filtering) with the following steps:

1. **Reads DICOM files** from the specified input folder.
2. **Constructs a 3D volume** by ordering the slices based on the DICOM Instance Number tag.
3. **Performs the convolution**: modifies the image and updates the DICOM tags.
4. **Saves the denoised DICOM files** in the specified output folder.

## About Convolution 2D in XNAT
Similar to 2D convolution but adapted to launch a container in XNAT.  
[Here](https://drive.google.com/drive/folders/1-TaOmXurFRz_Z5HH44pAyF7tUXEltCDP?usp=drive_link) is a video tutorial demonstrating its functionality in XNAT.

---




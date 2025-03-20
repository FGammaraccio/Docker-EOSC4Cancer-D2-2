# Docker-EOSC4Cancer-D2-2

## Prerequisites
* [Docker](https://www.docker.com/) 

## Usage
Follow these steps to build and run the Docker container:

1. **Clone the repository**
   ```sh
   git clone https://github.com/FGammaraccio/Docker-EOSC4Cancer-D2-2.git
   ```

2. **Navigate to the project directory**
   ```sh
   cd Docker-EOSC4Cancer-D2-2
   ```

3. **Build the Docker image**
   ```sh
   docker build -t snr ./snr
   ```
   This command creates a Docker image named `snr` from the `snr` directory.

4. **Run the container**
   ```sh
   docker run --rm \
     -v ./data/input/03-18-1995-NA-ECT008IV---CT-ABDOMEN-W-CO-59531/SCANS/2/DICOM:/input \
     -v ./data/output/output_snr:/output snr
   ```
   This command runs the container and mounts the input and output directories:
   - `./data/input/.../DICOM` is mapped to `/input` inside the container.
   - `./data/output/output_snr` is mapped to `/output` inside the container.
   - The `--rm` flag ensures the container is removed after execution.

## Data

### Input
The input consists of a single patient's CT scan in DICOM format. The scan is processed within the container.
Example dataset: [CT scan](https://xnat.health-ri.nl/app/action/DisplayItemAction/search_element/xnat%3ActSessionData/search_field/xnat%3ActSessionData.ID/search_value/BMIAXNAT_E87500/popup/false/project/eosc4cancer_tcga_coad)

### Output
- **SNR Output**: A text file containing the computed SNR.

## SNR Description
**SNR** is a tool designed to calculate the Signal-to-Noise Ratio (SNR). It performs the following steps:

1. **Reads DICOM files** from the specified input folder.
2. **Constructs a 3D volume** by ordering the slices based on the DICOM Instance Number tag.
3. **Computes the SNR** in the 3D volume using the formula:

\[ x
  = \dfrac{\dfrac{a}{b}}{c}
  = \dfrac{\frac{\textstyle a}{\textstyle b}}{c}
  = \dfrac{\frac{a}{b}}{c}
  \equiv \dfrac{\tfrac{a}{b}}{c}
\]

   - `i_avg` is the average intensity value at the center of the volume (using a kernel size of 5x5 pixels).
   - `σ_i` is the standard deviation of the background noise, calculated from a 5x5 pixel region in the top-left corner.

4. **Saves the SNR value** to a text file in the output folder.




---




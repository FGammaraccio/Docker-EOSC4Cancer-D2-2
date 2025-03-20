# Docker-EOSC4Cancer-D2-2

## Overview
This repository provides a Docker environment for computing the Signal-to-Noise Ratio (SNR) on patient CT scans.

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
- **SNR Output**: A text file containing the computed SNR is saved in the `/output` directory.



---




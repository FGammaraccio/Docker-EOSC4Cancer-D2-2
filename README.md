# Docker-EOSC4Cancer-D2-2
Docker images examples
## Prerequisites
* [Docker](https://www.docker.com/)

## Usage
1. Clone the repository
   ```sh
   git clone https://github.com/FGammaraccio/Docker-EOSC4Cancer-D2-2.git
   ```
2. Enter the Cloned Repository
   ```sh
   cd Docker-EOSC4Cancer-D2-2
   ```
3. Build the image
   ```sh
   docker build -t snr ./snr
   ```
4. Run the container
   ```sh
   docker run --rm -v .\data\input\03-18-1995-NA-ECT008IV---CT-ABDOMEN-W-CO-59531\SCANS\2\DICOM:/input -v .\data\output\output_snr:/output snr
   ```
   
## Data

### Input
Download CT scan from a single patient (e.g. [CT scan](https://xnat.health-ri.nl/app/action/DisplayItemAction/search_element/xnat%3ActSessionData/search_field/xnat%3ActSessionData.ID/search_value/BMIAXNAT_E87500/popup/false/project/eosc4cancer_tcga_coad))

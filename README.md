# Diffuse Neutrino Analysis Summer School Practicum

Welcome to the hands-on statistical analysis session. We will be using a legacy IceCube High-Energy Starting Event (HESE) toy dataset and simulation to perform a diffuse astrophysical flux fit, and a frequentist hypothesis test, comparing a Single Power Law flux model against a Log Parabola model.

# Getting Started

Click the badge below to launch the analysis environment in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vedant8/diffuse-neutrino-practicum/blob/main/exercises/diffuse_fit.ipynb)

## 📁 Repository Structure

* `exercises/diffuse_fit.ipynb`: The Primary workbook containing the analysis segments.
* `exercises/utils.py`: Background helper scripts for environment configuration.

## 📊 Datasets Used
You will need to uncomment the first four lines of the first cell, and then execute it
```python
# # Create a data directory and download the large file natively from Google Drive
# !mkdir -p ../data
# !gdown --id 1T8F576XAXluQ_UT5a0jQJzIbodB6i1I5 -O ../data/hese_toy_data.json
# !gdown --id 1VF1rG-hO1WA0SpA5NEEqmO24bVKl-Ftb -O ../data/hese_toy_simulation.json
```
The notebook will automatically download the following files into a `../data/` directory relative to your workspace:
1. `hese_toy_data.json` (~7KB): Simulated "experimental" high-energy events.
2. `hese_toy_simulation.json` (~200MB): The core simulation containing generation weights for reweighting spectral parameters.

---
*For issues or questions during the live session, please ping Dr. Basu.*
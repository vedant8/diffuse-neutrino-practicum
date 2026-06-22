# Diffuse Neutrino Analysis Summer School Practicum

Welcome to the hands-on statistical analysis session. We will be using a legacy IceCube High-Energy Starting Event (HESE) toy dataset and simulation to perform a diffuse astrophysical flux fit, and a frequentist hypothesis test, comparing a Single Power Law flux model against a Log Parabola model.

# Getting Started

Click the badge below to launch the analysis environment in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vedant8/diffuse-neutrino-practicum/blob/main/exercises/diffuse_fit.ipynb?v=1)

## Repository Structure

* `exercises/diffuse_fit.ipynb`: The Primary workbook containing the analysis segments.
* `exercises/utils.py`: Background helper scripts for environment configuration.

```
The notebook will automatically download the following files into a directory relative to your workspace:
1. `hese_toy_data.json` (~7KB): Simulated "experimental" high-energy events.
2. `hese_toy_simulation.json` (~200MB): The core simulation containing generation weights for reweighting spectral parameters.

---
*For issues or questions during the live session, please ping Dr. Basu.*
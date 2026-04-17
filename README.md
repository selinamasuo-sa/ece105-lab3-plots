<!--
Section list:
1. Project overview
2. Files
3. Dependencies and environment setup
4. How to run
5. Output files
6. AI tools used and disclosure
-->

# ECE105 Lab 3 Plots

## Project overview

`generate_plots.py` creates synthetic temperature sensor data and generates a single summary figure with three subplots:
- scatter plot of Sensor A and Sensor B vs. time
- overlaid histogram of Sensor A and Sensor B readings
- box plot comparing Sensor A and Sensor B distributions

The script uses a reproducible random seed (`1234`) and saves the figure to disk.

## Files

- `generate_plots.py`: data generation + plotting helpers + `main()` entry point
- `sensor_analysis.png`: output image created by the script

## Dependencies and environment setup

Activate your `ece105` Conda environment:

```bash
conda activate ece105
```

Install dependencies with either Conda or Mamba:

```bash
conda install numpy matplotlib
```

or

```bash
mamba install numpy matplotlib
```

## How to run

From this project directory:

```bash
python generate_plots.py
```

## Output files

Running the script produces:

- `sensor_analysis.png` — a 1x3 figure (scatter, histogram, box plot), saved at 150 DPI with a tight bounding box.

## AI tools used and disclosure

_Placeholder: Add your disclosure text here describing any AI tools used, what they were used for, and how you reviewed/validated the generated work._

I used GitHub Copilot as well as the code completion tools in VS Code for this assignment. I verified the work by parsing through the generated code to look for inconsistencies in importing modules; naming functions, variables, parameters, etc; and ran the program frequently to simulate problems.
Additionally, I asked prompted the AI to include some print statements such that I could verify the values of specific variables at various points in the program's runtime.

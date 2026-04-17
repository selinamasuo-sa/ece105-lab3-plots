"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

import numpy as np

def generate_data(seed: int = 1234, n: int = 200):
    """ Generate synthetic sensor data for two temperature sensors.

    Parameters
    ----------
    seed : int
        Seed for numpy.random.default_rng() for reproducibility.
    n : int
        Number of samples to generate for each sensor (default 200).

    Returns
    -------
    timestamps : numpy.ndarray
        1-D array of shape (n,) with dtype float64 containing sorted
    timestamps
        uniformly sampled from 0 to 10 seconds.
    sensor_a : numpy.ndarray
        1-D float64 array of shape (n,) with sensor A readings drawn from a
        normal distribution (mean=25.0, std=3.0).
    sensor_b : numpy.ndarray
        1-D float64 array of shape (n,) with sensor B readings drawn from a
        normal distribution (mean=27.0, std=4.5).

    Notes
    -----
    Uses numpy.random.default_rng for modern, reproducible RNG. Outputs are
    explicitly cast to float64 to match expected notebook types.
    """

    rng = np.random.default_rng(seed)
    timestamps = np.sort(rng.uniform(0.0, 10.0, n)).astype(np.float64)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n).astype(np.float64)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n).astype(np.float64)
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(ax, timestamps, sensor_a, sensor_b, label_a='Sensor A', label_b='Sensor B', title='Simulated temperature readings (scatter)'):
    """
    Draw a scatter plot of two sensors onto an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes object to draw into. Modified in place.
    timestamps : numpy.ndarray
        1-D array of shape (n,) with timestamps (seconds).
    sensor_a : numpy.ndarray
        1-D array of shape (n,) with Sensor A temperature readings (°C).
    sensor_b : numpy.ndarray
        1-D array of shape (n,) with Sensor B temperature readings (°C).
    label_a : str, optional
        Legend label for sensor A (default 'Sensor A').
    label_b : str, optional
        Legend label for sensor B (default 'Sensor B').
    title : str, optional
        Title to set on the axes.

    Returns
    -------
    None
        The function modifies the provided Axes in place and returns None.
    """
    # Local import for plotting utilities
    import matplotlib.pyplot as plt

    # Scatter points
    ax.scatter(timestamps, sensor_a, c='C0', marker='o', s=36, alpha=0.75, label=label_a)
    ax.scatter(timestamps, sensor_b, c='C1', marker='s', s=36, alpha=0.75, label=label_b)

    # Reference lines at the sample means
    ax.axhline(np.mean(sensor_a), color='C0', ls='--', lw=1)
    ax.axhline(np.mean(sensor_b), color='C1', ls='--', lw=1)

    # Labels, title, legend and grid
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    return None


def plot_histogram(ax, sensor_a, sensor_b, bins='auto', label_a='Sensor A', label_b='Sensor B', title='Histogram of Sensor A and Sensor B readings'):
    """
    Draw overlapping histograms for two sensors onto an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes object to draw into. Modified in place.
    sensor_a : numpy.ndarray
        1-D array of shape (n,) with Sensor A temperature readings (°C).
    sensor_b : numpy.ndarray
        1-D array of shape (n,) with Sensor B temperature readings (°C).
    bins : int or sequence or str, optional
        Binning specification passed to numpy.histogram_bin_edges / Axes.hist
        (default 'auto'). A common binning is computed from the combined data
        to facilitate comparison.
    label_a : str, optional
        Legend label for sensor A.
    label_b : str, optional
        Legend label for sensor B.
    title : str, optional
        Title to set on the axes.

    Returns
    -------
    None
        The function modifies the provided Axes in place and returns None.
    """
    import numpy as np

    # Compute common bins from combined data for fair comparison
    all_data = np.concatenate([sensor_a, sensor_b])
    bin_edges = np.histogram_bin_edges(all_data, bins=bins)

    ax.hist(sensor_a, bins=bin_edges, alpha=0.6, color='C0', label=label_a, edgecolor='black')
    ax.hist(sensor_b, bins=bin_edges, alpha=0.6, color='C1', label=label_b, edgecolor='black')

    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title(title)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    return None


def plot_boxplot(ax, sensor_a, sensor_b, labels=('Sensor A','Sensor B'), showmeans=True, title='Box plot of Sensor A and Sensor B readings'):
    """
    Draw a box plot comparing two sensors onto an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes object to draw into. Modified in place.
    sensor_a : numpy.ndarray
        1-D array of shape (n,) with Sensor A temperature readings (°C).
    sensor_b : numpy.ndarray
        1-D array of shape (n,) with Sensor B temperature readings (°C).
    labels : sequence of str, optional
        Labels for the two boxplot categories (default ('Sensor A','Sensor B')).
    showmeans : bool, optional
        If True, show the mean marker on each box (default True).
    title : str, optional
        Title to set on the axes.

    Returns
    -------
    None
        The function modifies the provided Axes in place and returns None.
    """
    # Use patch_artist=True to allow coloring if desired
    ax.boxplot([sensor_a, sensor_b], labels=labels, showmeans=showmeans, patch_artist=True)

    ax.set_ylabel('Temperature (°C)')
    ax.set_title(title)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    return None

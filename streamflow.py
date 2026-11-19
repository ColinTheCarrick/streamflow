# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    streamflow_data = np.genfromtxt(
        filename,
        delimiter=",",
        dtype=str,
        skip_header=1
    )

    dates = streamflow_data[1:, 0].astype("datetime64")
    flows = streamflow_data[1:, 1:].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    plt.figure(figsize=(10, 6))
    for column, site in enumerate(sites):
        plt.plot(dates, flows[:, column], label=site)

    plt.legend(title="Site Numbers")
    plt.title("Provo River Streamflow Data")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.ylabel("Streamflow (cfs)")
    plt.tight_layout()
    plt.grid(True)
    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
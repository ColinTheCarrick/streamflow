# -*- coding: utf-8 -*-
import csv
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

    dates = streamflow_data[:, 0].astype("datetime64")
    flows = streamflow_data[:, 1:].astype(float)
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
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()

# I used AI to write this section of the code.
# It uses three parameters to search within the CSV file and find the maximum, minimum, and average flow for each gauge.
def summarize(dates, flows, sites):
    # This sets the head to be equal to f strings and filers the data.
    header = (
        f"{'Gauge':<12}{'Max (cfs)':>10}   {'Date of max':<16} "
        f"{'Min (cfs)':>10} {'Avg (cfs)':>10}"
    )
    print(header)
    # This sets the head to be equal to f strings and filers the data.
    rows = []
    for column, site in enumerate(sites):
        gauge_flows = flows[:, column]
        max_index = np.argmax(gauge_flows)
        date_of_max = str(dates[max_index])
        date_of_max = date_of_max.replace("T", " ")[:16]
        maximum = np.max(gauge_flows)
        minimum = np.min(gauge_flows)
        average = np.mean(gauge_flows)
        # This prints the data in a formatted way and appends it to the rows list.
        print(
            f"{site:<12}{maximum:>10.1f}   {date_of_max:<16} "
            f"{minimum:>10.1f} {average:>10.1f}"
        )
        rows.append((site, f"{maximum:.1f}", date_of_max, f"{minimum:.1f}", f"{average:.1f}"))
    # This writes the data to a CSV file called streamflow_summary.csv.
    with open("streamflow_summary.csv", "w", newline="", encoding="utf-8") as summary_file:
        writer = csv.writer(summary_file)
        writer.writerow(["Gauge", "Max (cfs)", "Date of max", "Min (cfs)", "Avg (cfs)"])
        writer.writerows(rows)



# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)

#I used AI to write this section of the code.
# This is the variable that is displayed prompting the user to enter a flow threshold.
threshold = float(input("Enter a flow threshold (cfs): "))
# This prints the input statement.
print("\nHours above threshold:")
# This creates a for loop that iterates through the sites and counts the number of readings above the threshold, then calculates the hours above the threshold and prints it.
for column, site in enumerate(sites):
    readings_above_threshold = np.sum(flows[:, column] > threshold)
    hours_above_threshold = readings_above_threshold * 0.25
    print(f"{site}: {hours_above_threshold:.2f} hours")
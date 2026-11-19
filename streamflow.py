# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# I used AI to generate most of the code, then I compared it to the image in the instructions and filled in the difference
streamflow_data = np.genfromtxt(
    "June-2021-Provo-River-Streamflow-Rates.csv",
    delimiter=",",
    dtype=str, # This makes the variable into a string
    skip_header=1
)

x = streamflow_data[1:, 0].astype('datetime64') # I adjusted this from how it was written from the AI
# I added the astype to the variable above, and the 1 before the colon.
# Ask the TAs what this means and how I can apply this further.
y_1 = streamflow_data[1:, 1].astype(float)  # Site 10163000
y_2 = streamflow_data[1:, 2].astype(float)  # Site 10155200
y_3 = streamflow_data[1:, 3].astype(float)  # Site 10155500
y_4 = streamflow_data[1:, 4].astype(float)  # Site 10154200
y_5 = streamflow_data[1:, 5].astype(float)  # Site 10155000

# Again used AI to write the bulk of the code and made adjustments as I tested
plt.figure(figsize=(10, 6))
plt.plot(x, y_1, label='10163000') # I adjust the labels for these after the AI wrote them
plt.plot(x, y_2, label='10155200')
plt.plot(x, y_3, label='10155500')
plt.plot(x, y_4, label='10154200')
plt.plot(x, y_5, label='10155000')

plt.legend(title='Site Numbers') # title = added the title here just for the legend itself
plt.title("Provo River Streamflow Data")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.ylabel("Streamflow (cfs)")
plt.tight_layout() # I added this to make it tighter
plt.grid(True) # I added this to show the grid
plt.show()
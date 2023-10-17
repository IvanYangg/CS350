import numpy as np
import matplotlib.pyplot as plt
import math

lines = ""
rejectedTimestamps = []
interRejectionTimes = []

# Read the input file
with open('src/1e.txt', 'r') as file:
    lines = file.readlines()

# Iterate through lines and parse request lengths
for line in lines:
    if line.startswith("X"):
        parts = line.split(":")[1]
        rejectedTimestamps.append(float(parts.split(",")[-1][:-1]))

for i in range(1, len(rejectedTimestamps)):
    interRejectionTimes.append(rejectedTimestamps[i] - rejectedTimestamps[i-1])

bins = np.arange(0, 20.5, 0.05)  # Create bins from 0 to 25 with 0.5 increments

# Create the histogram
plt.figure(figsize=(10, 6))  # Set the figure size
plt.hist(interRejectionTimes, bins=bins, edgecolor='k', alpha=0.75)

# Add labels and a title
plt.xlabel('Inter-Rejection Time Ranges')
plt.ylabel('Frequency')
plt.title('Distribution of Data With Constrained Queues')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
print("Percentage of requests that get rejected: ", (len(rejectedTimestamps)/1500) * 100)

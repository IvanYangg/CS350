import numpy as np
import matplotlib.pyplot as plt
import math


lines = ""
# Read the input file
with open('src/1b.txt', 'r') as file:
    lines = file.readlines()

#variables for plot
ranges = {}  
lengths = []
counted = []  

sentTimes = [] 
interArrival = []

# helper function to generate the ranges and add them to the dictionary, ranges.
def generateLengthRanges(start, end, increment):
    while start < end:
        range_str = f"{start:.3f}-{start + increment:.3f}"
        ranges[range_str] = (start, start + increment)
        start += increment


#function to plot request lengths 
def requestLengths():
    total = 0
    maxLength = 0
    requests = 0
    data = []
    generateLengthRanges(0.000,0.500,0.01)
    counters = {key: 0 for key in ranges}
    # Iterate through lines and parse request lengths
    for line in lines:
        if line.startswith("R"):
            parts = line.split(":")
            if len(parts) == 2:
                _, length_part = parts
                length = float(length_part.split(",")[1])
                data.append(length)
                requests += 1
                total += length
                maxLength = max(maxLength, length)
                for key, (start, end) in ranges.items():
                    if start <= length < end:
                        counters[key] += 1
    # Print the counts for each range
    for key, count in counters.items():
        lengths.append(key)
        counted.append(count / 1500)
    mean = total/requests
    differences = [(x - mean) ** 2 for x in data]
    variance = sum(differences) / len(data)
    standardDev = math.sqrt(variance)

    plt.figure(figsize=(10, 6))  # Set the figure size

    # Create a bar plot
    plt.bar(lengths, counted)
    plt.xlabel('Request Length Ranges')
    plt.ylabel('Accumulated Counts (in thousands)')
    plt.title('Accumulated Request Lengths')
    plt.xticks(rotation=80)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

    return standardDev

#function to plot inter-arrival times 
def inter_arrival_time():
    total = 0
    generateLengthRanges(0.000,2.000,0.005)
    counters = {key: 0 for key in ranges}
    for line in lines:
        if line.startswith("R"):
            parts = line.split(":")
            if len(parts) == 2:
                _, length_part = parts
                length = float(length_part.split(",")[0])
                sentTimes.append(length)
    for i in range(1, len(sentTimes)):
        interArrival.append(sentTimes[i] - sentTimes[i-1])
    for time in interArrival:
        total += time
        for key, (start, end) in ranges.items():
            if start <= time < end:
                counters[key] += 1
    # Print the counts for each range
    for key, count in counters.items():
        lengths.append(key)
        counted.append(count/1500)
    
    mean = total / len(interArrival)
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(lengths, counted, color='skyblue')
    plt.xlabel('Inter-Arrival (Time bins)')
    plt.ylabel('Count')
    plt.title('Inter-Arrival Times vs. Count')
    plt.xticks(rotation=80, ha='right')
    plt.xticks(range(0, 410, 10))
    plt.tight_layout()

    plt.show()

    return 1/mean    #lambda value
print(inter_arrival_time())

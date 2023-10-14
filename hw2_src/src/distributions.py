import numpy as np
import matplotlib.pyplot as plt

lines = ""
# Read the input file
with open("1a.txt", "r") as file:
    lines = file.readlines()

#variables for plot
ranges = {}  
lengths = []
counted = []  

sentTimes = [] #1b variables
interArrival = []
#helper function
def eval2b(lines):
    

# helper function to generate the ranges and add them to the dictionary, ranges.
def generateLengthRanges(start, end, increment):
    while start < end:
        range_str = f"{start:.3f}-{start + increment:.3f}"
        ranges[range_str] = (start, start + increment)
        start += increment

#function to plot request lengths (1a)
def requestLengths():
    maxLength = 0
    generateLengthRanges(0.000,1.000,0.005)
    counters = {key: 0 for key in ranges}
    # Iterate through lines and parse request lengths
    for line in lines:
        if line.startswith("R"):
            parts = line.split(":")
            if len(parts) == 2:
                _, length_part = parts
                length = float(length_part.split(",")[1])
                maxLength = max(maxLength, length)
                for key, (start, end) in ranges.items():
                    if start <= length < end:
                        counters[key] += 1
    # Print the counts for each range
    for key, count in counters.items():
        lengths.append(key)
        counted.append(count / 1000)
    return maxLength

#function to plot inter-arrival times (1b)
def inter_arrival_time():
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
        for key, (start, end) in ranges.items():
            if start <= time < end:
                counters[key] += 1
    # Print the counts for each range
    for key, count in counters.items():
        lengths.append(key)
        counted.append(count/999)
    
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
# inter_arrival_time()

def distributionPlots():
    maxLengthValue = requestLengths()

    bins = np.linspace(0, 1.5, 151)
    freq, bin_edges = np.histogram(lengths, bins=bins, density=True)
    plt.plot(bin_edges[:-1], freq, label='Server Data', linewidth=2)
  
    # Normal distribution
    normal_samples = np.random.normal(0.1, 1, 10000)
    freq, bin_edges = np.histogram(normal_samples, bins=bins, density=True)
    plt.plot(bin_edges[:-1], freq, label='Normal Distribution', linewidth=2)
  
    # Exponential distribution
    exponential_samples = np.random.exponential(0.1, 10000)
    freq, bin_edges = np.histogram(exponential_samples, bins=bins, density=True)
    plt.plot(bin_edges[:-1], freq, label='Exponential Distribution', linewidth=2)
  
    # Uniform distribution
    uniform_samples = np.random.uniform(0, 0.2, 10000)  # mean=0.1, so min=0, max=0.2
    freq, bin_edges = np.histogram(uniform_samples, bins=bins, density=True)
    plt.plot(bin_edges[:-1], freq, label='Uniform Distribution', linewidth=2)
  
    plt.xlabel('Request Length')
    plt.ylabel('Density')
    plt.title('Comparison of Different Distributions')
    plt.legend()
    plt.show()
# distributionPlots()
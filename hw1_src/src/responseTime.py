import numpy as np

# counter variable to track total response time
responseTime = 0
maxResponseTime = 0
minResponseTime = 2**31
stdev = []
# Open the text file for reading
with open('src/util12.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line by comma 
        parts = line.split(',')
        sentTimestamp = (parts[0]).split(':')
        completionTimestamp = float(parts[3])
        # update current total of busy time and min and max variables
        minResponseTime = min(minResponseTime, (completionTimestamp - float(sentTimestamp[1])))
        maxResponseTime = max(maxResponseTime, (completionTimestamp - float(sentTimestamp[1])))
        stdev.append(completionTimestamp - float(sentTimestamp[1]))
        responseTime += (completionTimestamp - float(sentTimestamp[1]))
# Print average response time
print("Average Response Time: ", responseTime / 500)
# print("Min Response Time: ", minResponseTime)
# print("Max Response Time: ", maxResponseTime)
# print("Standard Deviation: ", np.std(stdev))


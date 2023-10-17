# counter variable to track total response time
responseTime = 0
serverStartTime = 0
serverTotalTime = 0
timeBusy = 0
completionTimestamp = 0
# Open the text file for reading
with open('src/build/a19d1.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        if line.startswith("R"):
            # Split the line by comma 
            parts = line.split(',')
            requestLength = parts[1]
            timeBusy += float(requestLength)
            sentTimestamp = (parts[0]).split(':')
            request = sentTimestamp[0]
            if request == 'R1':
                serverStartTime = float(sentTimestamp[1])
            completionTimestamp = float(parts[4])
            # update current total of busy time
            responseTime += (completionTimestamp - float(sentTimestamp[1]))
serverTotalTime = completionTimestamp - serverStartTime
# Print average response time
print("Average Response Time: ", responseTime / 1500)
print("Total Utilization of Server: ", timeBusy / serverTotalTime)
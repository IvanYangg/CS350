# Function to process the output and separate it into T0 and T1
def separate_worker_output(filename):
    t0_output = []
    t1_output = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    current_thread = None
    for line in lines:
        if line.startswith("T0"):
            current_thread = t0_output
        elif line.startswith("T1"):
            current_thread = t1_output

        # Skip lines starting with "Q:"
        if not line.startswith("Q:"):
            current_thread.append(line)

    return t0_output, t1_output

# Print the separated output
def parse(output):
    initialTime = (output[0].split(","))[2]
    endTime = (output[-1].split(","))[-1]
    totalTime = float(endTime) - float(initialTime)
    timeBusy = 0
    for line in output:
        timeBusy += float((line.split(","))[1])
    return timeBusy / totalTime

#Calculate average response times for n number of threads 
def avgResponseTime(files):
    averageResponseTimes = []
    for file in files:
        totalResponseTime = 0
        numRequests = 0
        with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Skip lines starting with "Q:"
                if not line.startswith("Q:"):
                    completion_ts = float(line.split(",")[-1])
                    sent_ts = float(line.split(",")[0].split(":")[-1])
                    totalResponseTime += (completion_ts - sent_ts)
                    numRequests += 1
        averageResponseTimes.append(totalResponseTime/numRequests)
    return averageResponseTimes

#Calculate rejection rates
def numRejects(files):
    rejections = []
    for file in files:
        rejectRequests = 0
        with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("X"):
                    rejectRequests += 1
        rejections.append(rejectRequests/1500)
    return rejections

def main():
    # Specify the filename of the text file containing the output
    filename = 'part1b.txt'
    utilization = []
    # Call the function to separate the output
    t0_output, t1_output = separate_worker_output(filename)
    # parse data
    utilization.append(parse(t0_output))
    utilization.append(parse(t1_output))
    #results
    # print(utilization)
    #used for avgResponseTime() and part1b.txt contains output for when w = 2
    files = ['part1b.txt', 'w4.txt', 'w6.txt', 'w8.txt']
    # print(avgResponseTime(files))

    #used for part d/ reject files
    rejectFiles = ['part1d-1.txt', 'part1d-2.txt']
    print(numRejects(rejectFiles))
main()

# counter variable to track total busy time
total_busy_time = 0
receiptTimestamp = 0
completionTimestamp = 0
# Open the text file for reading
with open('src/server.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line by comma and get the second attribute as a float
        parts = line.split(',')
        if receiptTimestamp == 0:
            receiptTimestamp = float(parts[2])
        busy_time = float(parts[1])
        completionTimestamp = float(parts[3])
        
        # update current total of busy time
        total_busy_time += busy_time
# Print total busy time
print(f"Total Busy Time: {total_busy_time/(completionTimestamp - receiptTimestamp)}")

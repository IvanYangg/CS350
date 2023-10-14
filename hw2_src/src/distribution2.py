import queue
import re
import matplotlib.pyplot as plt

def parse_data_from_file(file_path):
    # Initialize data structures to store the parsed information
    q_lengths = []
    r_data = []

    # Define regular expressions for matching Q and R patterns
    q_pattern = r'Q:\[(.*?)\]'
    r_pattern = r'R(\d+):(\d+\.\d+,\d+\.\d+,\d+\.\d+,\d+\.\d+)'

    try:
        with open(file_path, 'r') as file:
            data = file.read()

            # Find and store the Q and R information
            for match in re.finditer(q_pattern, data):
                q_data_str = match.group(1).strip()
                if q_data_str:
                    q_data_list = [item.strip() for item in q_data_str.split(',')]
                    q_lengths.append(len(q_data_list))
                else:
                    q_lengths.append(0)  # Handle empty list case

            for match in re.finditer(r_pattern, data):
                r_num = match.group(1)
                r_values_str = match.group(2)
                r_values = [float(value) for value in r_values_str.split(',')]
                r_data.append({
                    'request_number': f'R{r_num}',
                    'sent_timestamp': r_values[0],
                    'request_length': r_values[1],
                    'receipt_timestamp': r_values[2],
                    'completion_timestamp': r_values[3]
                })

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return q_lengths, r_data

def eval2B(file_path):
    file_path = './src/build/' + file_path  # Replace with the path to your text file
    q_lengths, r_data = parse_data_from_file(file_path)
    rcount=0
    total_time = r_data[-1]["completion_timestamp"] - r_data[0]["receipt_timestamp"]
    total_queue = 0 
    busy_time = 0.0
    aggregate_response_time = 0.0
    for i in range(999):
        total_queue += q_lengths[i] * ((r_data[i+1]["completion_timestamp"]-r_data[i]["completion_timestamp"]))
        rcount += q_lengths[i] * ((r_data[i+1]["completion_timestamp"]-r_data[i]["completion_timestamp"])/total_time)
        busy_time+=r_data[i]["request_length"]
        aggregate_response_time += r_data[i]["completion_timestamp"] - r_data[i]["sent_timestamp"]
    utilization = (busy_time/total_time)*100
    average_response_time = aggregate_response_time/1000
    average_queue_length = rcount 
    return (utilization, average_response_time, average_queue_length)




# Example usage:
file_path = 'serverq14.txt'  # Replace with the path to your text file
q_lengths, r_data = parse_data_from_file(file_path)

# Print the extracted data
print("Q Lengths:", q_lengths)
print("R Data:", r_data)
rcount=0
print(len(r_data),len(q_lengths))
print(r_data[0], q_lengths[0])
total_time = r_data[-1]["completion_timestamp"] - r_data[0]["receipt_timestamp"]
total_queue = 0 
for i in range(999):
    total_queue += q_lengths[i] * ((r_data[i+1]["completion_timestamp"]-r_data[i]["completion_timestamp"]))
    rcount += q_lengths[i] * ((r_data[i+1]["completion_timestamp"]-r_data[i]["completion_timestamp"])/total_time)
print(rcount)
print(total_queue, total_time)
"""
utilization_values = []
average_response_times = []  # Average response times corresponding to each utilization level
average_queue_sizes = [] # Average queue sizes corresponding to each utilization level
for i in range(1,16):
    path = "output"
    utilization, average_response_time, average_queue_length = eval2B(path + str(i) + ".txt")
    utilization_values += [utilization]
    average_response_times += [average_response_time]
    average_queue_sizes += [average_queue_length]
    print("-a set to ", i, " STATS:\n")
    print("Utilization: ", utilization, "%\n")
    print("Average Response Time: ", average_response_time, "\n")
    print("Average Queue Length: ", average_queue_length, "\n")
    print("-----------------------------")

# Example data (replace with your actual data)


# Create a plot with two y-axes
fig, ax1 = plt.subplots()

# Plot average response time on the first y-axis (line 1)
ax1.set_xlabel('Server Utilization')
ax1.set_ylabel('Average Response Time', color='tab:blue')
ax1.plot(utilization_values, average_response_times, color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis sharing the same x-axis
ax2 = ax1.twinx()

# Plot average queue size on the second y-axis (line 2)
ax2.set_ylabel('Average Queue Size', color='tab:red')
ax2.plot(utilization_values, average_queue_sizes, color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Add labels and title
plt.xlabel('Server Utilization')
plt.title('Average Response Time and Average Queue Size vs. Server Utilization')

# Show the plot
plt.show()
"""
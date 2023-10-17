import matplotlib.pyplot as plt

# Data for Line 1
line1_x = [0.492228383, 0.541363104, 0.588954403, 0.63896453, 0.687453725, 0.737034863, 0.785776661, 0.834161183, 0.882121785, 0.9314688]
line1_y = [0.098025667, 0.108037881, 0.128655053, 0.134137067, 0.160476593, 0.194758339, 0.290055395, 0.298868479, 0.404208451, 0.630414808]

# Data for Line 2
line2_x = [0.50717008, 0.557730519, 0.608088102, 0.658749563, 0.709403169, 0.759574851, 0.810613784, 0.859768673, 0.911216794, 0.956558581]
line2_y = [0.075609365, 0.081071702, 0.087629861, 0.095072929, 0.105188492, 0.118437256, 0.139521785, 0.178845275, 0.252833838, 0.490721295]

# Create a line graph
plt.figure(figsize=(8, 6))  # Set the figure size

# Plot Line 1
plt.plot(line1_x, line1_y, label='d=0', marker='o')

# Plot Line 2
plt.plot(line2_x, line2_y, label='d=1', marker='s')

# Add labels and a legend
plt.xlabel('Server Utilization')
plt.ylabel('Average Response Time')
plt.title('Effect of Distribution Parameter')
plt.legend()

plt.grid()  # Add grid lines if needed

# Display the plot
plt.show()

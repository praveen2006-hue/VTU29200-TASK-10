import matplotlib.pyplot as plt

# Define the data
intervals = ['140-145', '145-150', '150-155', '155-160', '160-165', '165-170', '170-175', '175-180', '180-185', '185-190']
frequencies = [2, 5, 15, 31, 46, 53, 45, 28, 21, 4]

# Plot the histogram (using a bar chart)
plt.bar(intervals, frequencies, edgecolor='red')
plt.xlabel('Height Intervals (cm)')
plt.ylabel('Frequency')
plt.title('Height Distribution Histogram')
plt.grid(True, axis='y')  # Adds horizontal grid lines for readability
plt.show()

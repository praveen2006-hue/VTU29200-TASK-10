import matplotlib.pyplot as plt

# Define the data
sizes = [35, 25, 25, 15]
mylabels = ['w', 'x', 'y', 'z']
myexplode = [0.2, 0, 0, 0]

# Plot the pie chart
# 'autopct' automatically formats and displays percentage values on each slice.
plt.pie(sizes, labels=mylabels, explode=myexplode, shadow=True, autopct='%1.1f%%')

plt.title('Pie Chart')
plt.show()

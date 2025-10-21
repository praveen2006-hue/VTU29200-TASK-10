import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2*pi
# This line generates an array of 1000 evenly spaced values between 0 and 2π.
# It takes three arguments: the starting point (0), the ending point (2*np.pi),
# and the number of points to generate (1000).
# It returns an array of equally spaced points between the start and end points, inclusive.
x = np.linspace(0, 2*np.pi, 1000)

# Generate y values corresponding to sine of x
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)  # Turns on the grid lines
plt.show()

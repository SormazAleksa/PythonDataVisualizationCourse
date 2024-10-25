# Import libraries

import matplotlib.pyplot as plt
import numpy as np

# Define x and y coordinates

x_value = np.random.random(50) * 100
y_value = np.random.random(50) * 100

# This declaration will create an array of 50 values ranging from 0 to 100 in float
# You can check that by printing x and y values, but every time you run this code the values will be different


plt.plot()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.scatter(x_value, y_value)
plt.show()

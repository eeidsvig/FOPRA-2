import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

# Path to the uploaded file
file_path = 'sample.txt'

# Initialize lists to store x and y values
x_values = []
y_values = []

# Read the file
with open(file_path, 'r') as file:
# Skip the first two lines
	next(file)
	next(file)
	# Read the remaining lines
	for line in file:
		# Split the line into x and y values
		x, y = map(float, line.strip().split())
		x_values.append(x)			
		y_values.append(y)


# Plotting
plt.figure(figsize=(10, 6))
plt.xlim([0, 2000])
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
#plt.scatter(x_values, y_values)
plt.title('Background')
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.grid(True)
plt.show()

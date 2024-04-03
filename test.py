import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
# Path to the uploaded file
file_path = 'calib_co60.txt'

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
plt.plot(x_values, y_values, linestyle='-', color='b')
plt.title('Spectrum')
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.grid(True)
plt.show()




# Gaussian function to fit
def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) ** 2) / (2 * stddev ** 2))

# Function to fit Gaussian to specified peak ranges
def fit_gaussians_to_peaks(y, peak_ranges):
    fit_params = []

    for start, end in peak_ranges:
        x_range = np.arange(start, end + 1)
        y_range = y[start:end + 1]

        # Initial guesses: max amplitude, center of range, estimate of stddev
        initial_guess = [max(y_range), np.mean(x_range), 1]

        try:
            # Fit the Gaussian model to the data
            params, _ = curve_fit(gaussian, x_range, y_range, p0=initial_guess)
            fit_params.append(params)
        except RuntimeError as e:
            print(f"Fit failed for peak range {start}-{end}: {e}")

    return fit_params

# Plotting function
def plot_data_and_fits(y, fit_params):
    plt.figure(figsize=(12, 6))
    plt.plot(y, label='Original Data', color='black')

    x_vals = np.arange(len(y))
    for params in fit_params:
        plt.plot(x_vals, gaussian(x_vals, *params), label=f'Gaussian fit around {params[1]:.0f}', linestyle='--')

    plt.title('Original Data with Fitted Gaussians')
    plt.xlabel('Channel')
    plt.ylabel('Counts')
    plt.legend()
    plt.show()

# Load your data here (for demonstration, this part is commented out)
file_path = 'calib_co60.txt'
data = np.loadtxt(file_path)
y = data[:, 1]  # Assuming the second column has the y-values

# Define the peak ranges you're interested in
peak_ranges = [(3980, 3982), (4492, 4495)]

# Fit Gaussians to these peaks
fit_params = fit_gaussians_to_peaks(y, peak_ranges)

# Plot the original data and the fitted Gaussians
plot_data_and_fits(y, fit_params)

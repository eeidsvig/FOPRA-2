from sklearn.linear_model import LinearRegression

# Define your data points
x = [356, 80]
y = [1353, 469]

# Reshape x into a 2D array for fitting
X = [[i] for i in x]  # This creates a 2D array, as required by scikit-learn

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Get the slope (m) and intercept (b) coefficients
m = model.coef_[0]
b = model.intercept_

# Print the equation in the desired format
print(f"y = {m:.2f}x + {b:.2f}")

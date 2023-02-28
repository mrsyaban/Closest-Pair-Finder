import matplotlib.pyplot as plt
import numpy as np

# Generate one-dimensional data
x = np.random.rand(100)

# Create scatter plot
plt.scatter(x, np.zeros_like(x))

# Set plot title and axis labels
plt.title('One-dimensional Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.show()
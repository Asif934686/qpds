import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)

# Create scatter plot
plt.scatter(x, y)

# Title and labels
plt.title("Random Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Display plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate random values
x = np.random.rand(50)
y = np.random.rand(50)

# Scatter plot with empty circles
plt.scatter(x, y, facecolors='none', edgecolors='blue')

plt.title("Scatter Plot with Empty Circles")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

plt.show()

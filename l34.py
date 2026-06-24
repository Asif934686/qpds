import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.randint(50, 500, 50)

# Scatter plot with different sized balls
plt.scatter(x, y, s=sizes)

plt.title("Scatter Plot with Different Sized Balls")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

plt.show()

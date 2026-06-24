import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Top plot
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title("Top Plot")

# Bottom left plot
plt.subplot(2, 3, 4)
plt.plot(x, y)

# Bottom middle plot
plt.subplot(2, 3, 5)
plt.plot(x, y)

# Bottom right plot
plt.subplot(2, 3, 6)
plt.plot(x, y)

plt.tight_layout()
plt.show()

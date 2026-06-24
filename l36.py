import matplotlib.pyplot as plt

# Group 1
weight1 = [55, 60, 65, 70, 75]
height1 = [150, 155, 160, 165, 170]

# Group 2
weight2 = [50, 58, 63, 68, 72]
height2 = [148, 153, 158, 163, 168]

# Group 3
weight3 = [45, 52, 57, 62, 67]
height3 = [145, 150, 155, 160, 165]

# Scatter plots
plt.scatter(weight1, height1, label='Group 1')
plt.scatter(weight2, height2, label='Group 2')
plt.scatter(weight3, height3, label='Group 3')

plt.title("Weight vs Height Comparison")
plt.xlabel("Weight (kg)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid(True)

plt.show()

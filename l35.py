import matplotlib.pyplot as plt

# Marks of 10 students
math_marks = [88, 72, 93, 85, 69, 78, 90, 76, 84, 95]
science_marks = [91, 70, 89, 87, 65, 80, 92, 75, 82, 96]

# Scatter plot
plt.scatter(math_marks, science_marks)

plt.title("Mathematics vs Science Marks")
plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")
plt.grid(True)

plt.show()

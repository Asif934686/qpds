import matplotlib.pyplot as plt
import numpy as np

# Data
men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)

# Group labels
groups = ['G1', 'G2', 'G3', 'G4', 'G5']

# X positions
x = np.arange(len(groups))
width = 0.35

# Create bars
plt.bar(x - width/2, men_means, width, label='Men')
plt.bar(x + width/2, women_means, width, label='Women')

# Labels and title
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, groups)
plt.legend()

# Display chart
plt.show()

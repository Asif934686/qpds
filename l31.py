import matplotlib.pyplot as plt
import numpy as np

# Data
men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)

men_std = (4, 3, 4, 1, 5)
women_std = (3, 5, 2, 3, 3)

groups = ['G1', 'G2', 'G3', 'G4', 'G5']
x = np.arange(len(groups))

# Create stacked bar chart
plt.bar(x, men_means, yerr=men_std, label='Men')
plt.bar(x, women_means, bottom=men_means,
        yerr=women_std, label='Women')

# Labels and title
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.xticks(x, groups)
plt.legend()

# Display chart
plt.show()

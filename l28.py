import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create horizontal bar chart
plt.barh(languages, popularity)

# Title and labels
plt.title("Popularity of Programming Languages")
plt.xlabel("Popularity (%)")
plt.ylabel("Programming Languages")

# Display chart
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 9]
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)
sizes = np.random.randint(10, 100, 100)
colors = np.random.rand(100)
pie_labels = ['Apple', 'Banana', 'Cherry', 'Date']
pie_sizes = [15, 30, 45, 10]
hist_data = np.random.randn(1000)

# Line Plot
plt.figure(figsize=(10, 8))

plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title('Line Plot')

# Bar Plot
plt.subplot(2, 3, 2)
plt.bar(categories, values)
plt.title('Bar Plot')

# Scatter Plot
plt.subplot(2, 3, 3)
plt.scatter(x_scatter, y_scatter, s=sizes, c=colors, alpha=0.5)
plt.title('Scatter Plot')

# Pie Chart
plt.subplot(2, 3, 4)
plt.pie(pie_sizes, labels=pie_labels, autopct='%1.1f%%')
plt.title('Pie Chart')

# Histogram
plt.subplot(2, 3, 5)
plt.hist(hist_data, bins=30)
plt.title('Histogram')

# Box Plot
plt.subplot(2, 3, 6)
plt.boxplot([np.random.randn(50), np.random.randn(50), np.random.randn(50)])
plt.title('Box Plot')

plt.tight_layout()
plt.show()

# Additional plots: Area Plot
plt.figure()
plt.fill_between(x, y, alpha=0.5)
plt.title('Area Plot')
plt.show()

# Violin Plot (requires seaborn, but can use matplotlib)
# For simplicity, skipping advanced ones, but matplotlib has violinplot
plt.figure()
plt.violinplot([np.random.randn(100), np.random.randn(100)])
plt.title('Violin Plot')
plt.show()

# Contour Plot
x_cont = np.linspace(-3, 3, 100)
y_cont = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x_cont, y_cont)
Z = np.sin(X) * np.cos(Y)
plt.figure()
plt.contour(X, Y, Z)
plt.title('Contour Plot')
plt.show()

# 3D Plot (requires mpl_toolkits)
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.title('3D Surface Plot')
plt.show()
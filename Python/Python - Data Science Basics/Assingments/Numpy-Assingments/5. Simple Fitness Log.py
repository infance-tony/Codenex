import numpy as np

# Weight log over 7 days
weight = np.array([78.5, 78.3, 78.6, 78.2, 78.0, 77.8, 77.9])

# Calculate weekly average
weekly_average = np.mean(weight)
print(f"Weekly average weight: {weekly_average}")

# Find differences between consecutive days
diffs = np.diff(weight)

# Max drop: the largest decrease (most negative diff)
max_drop = -np.min(diffs)  # Since min diff is most negative, -min gives the drop
print(f"Max drop between consecutive days: {max_drop}")

# Number of days with decrease
decreases = np.sum(diffs < 0)
print(f"Number of days showing a decrease: {decreases}")

import numpy as np

grocery = np.array([850, 920, 790, 1000, 880, 950])

# Average weekly spending
average_spending = np.mean(grocery)
print(f"Average weekly spending: ₹{average_spending:.2f}")

# Total spending
total_spending = np.sum(grocery)
print(f"Total spending: ₹{total_spending}")

# Week with highest spending (index)
highest_week_index = np.argmax(grocery)
print(f"Week with highest spending: Week {highest_week_index + 1} (index {highest_week_index})")

# Weeks spent above ₹900
weeks_above_900 = np.sum(grocery > 900)
print(f"Number of weeks spent above ₹900: {weeks_above_900}")
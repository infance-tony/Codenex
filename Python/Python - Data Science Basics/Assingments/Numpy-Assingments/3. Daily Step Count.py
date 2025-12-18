import numpy as np

steps = np.array([4200, 5600, 6100, 7100, 8200, 10200, 9500, 7800, 12000, 4500])

# Count how many days you walked > 8000 steps
days_over_8000 = np.sum(steps > 8000)
print(f"Days with > 8000 steps: {days_over_8000}")

# Find the mean & median of steps
mean_steps = np.mean(steps)
median_steps = np.median(steps)
print(f"Mean steps: {mean_steps}")
print(f"Median steps: {median_steps}")

# Replace any value < 5000 with the mean steps (vectorized)
steps_updated = np.where(steps < 5000, mean_steps, steps)
print(f"Updated steps: {steps_updated}")
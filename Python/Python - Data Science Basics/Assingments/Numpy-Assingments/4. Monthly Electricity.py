import numpy as np

# Units consumed for 6 months
units = np.array([210, 230, 180, 260, 245, 300])

# Task 1: Total consumption
total_consumption = np.sum(units)
print(f"Total consumption: {total_consumption} units")

# Task 2: Bill per month at ₹6 per unit
rate = 6
bill_per_month = units * rate
print(f"Bill per month: {bill_per_month}")

# Task 3: Identify months above 250 units
above_250 = units > 250
months_above_250 = np.where(above_250)[0] + 1  # Months starting from 1
print(f"Months above 250 units: {months_above_250}")

# Task 4: Apply 5% surcharge to months above 250
surcharge = np.where(above_250, bill_per_month * 0.05, 0)
final_bill = bill_per_month + surcharge
print(f"Final bill per month (with surcharge): {final_bill}")

import pandas as pd

# Grocery Store Sales
data_grocery = {
    'day': [1, 1, 2, 2],
    'product': ['Apple', 'Orange', 'Apple', 'Orange'],
    'qty': [10, 5, 8, 7],
    'price': [30, 20, 30, 20]
}
df_grocery = pd.DataFrame(data_grocery)
# Calculate total revenue per row (qty * price).
df_grocery['revenue'] = df_grocery['qty'] * df_grocery['price']
# Compute total sales per day.
total_sales_per_day = df_grocery.groupby('day')['revenue'].sum()
# Find which product has the highest total units sold.
total_units = df_grocery.groupby('product')['qty'].sum()
highest_product = total_units.idxmax()
print("Grocery:")
print(df_grocery)
print("Total sales per day:", total_sales_per_day)
print("Product with highest units:", highest_product)

# Employee Salary Data
data_emp = {
    "name": ["Anu", "Rahul", "Priya", "Vishal"],
    "department": ["HR", "IT", "IT", "Finance"],
    "salary": [32000, 55000, 60000, 45000]
}
df_emp = pd.DataFrame(data_emp)
# Display the average salary.
avg_salary = df_emp['salary'].mean()
# Sort employees by salary (descending).
sorted_emp = df_emp.sort_values('salary', ascending=False)
# Group by department → show mean salary.
dept_mean = df_emp.groupby('department')['salary'].mean()
# Filter only employees with salary > 50,000.
high_salary = df_emp[df_emp['salary'] > 50000]
print("\nEmployee:")
print("Avg salary:", avg_salary)
print("Sorted:", sorted_emp)
print("Dept mean:", dept_mean)
print("High salary:", high_salary)

# Student Marks Analysis
data_stud = {
    "name": ["Asha", "Rohan", "Manu", "Swathi", "Deepa"],
    "math": [81, 56, 75, 92, 60],
    "science": [78, 67, 72, 88, 55],
    "english": [85, 69, 70, 90, 65]
}
df_stud = pd.DataFrame(data_stud)
# Compute total marks per student.
df_stud['total'] = df_stud[['math', 'science', 'english']].sum(axis=1)
# Add a column average.
df_stud['average'] = df_stud[['math', 'science', 'english']].mean(axis=1)
# Find the student with the highest total.
highest_total = df_stud.loc[df_stud['total'].idxmax(), 'name']
# Select students with average ≥ 75.
avg_75 = df_stud[df_stud['average'] >= 75]
print("\nStudent:")
print(df_stud)
print("Highest total:", highest_total)
print("Avg >=75:", avg_75)

# House Rent Dataset
df_house = pd.DataFrame({
    "city": ["Tvm", "Kochi", "Tvm", "Kochi", "Kollam"],
    "rooms": [2, 3, 2, 1, 4],
    "rent": [11000, 18000, 9500, 8500, 22000]
})
# What is the average rent per city?
avg_rent_city = df_house.groupby('city')['rent'].mean()
# List houses with rent > ₹10,000.
rent_10k = df_house[df_house['rent'] > 10000]
# Which city has the maximum average rent?
max_avg_city = avg_rent_city.idxmax()
# Sort houses by number of rooms.
sorted_rooms = df_house.sort_values('rooms')
print("\nHouse:")
print("Avg rent per city:", avg_rent_city)
print("Rent >10k:", rent_10k)
print("City with max avg rent:", max_avg_city)
print("Sorted by rooms:", sorted_rooms)

# Bank Customer Transactions
data_bank = {
    'acc_id': [101, 102, 101, 102],
    'type': ['deposit', 'deposit', 'withdraw', 'withdraw'],
    'amount': [1000, 1500, 300, 600],
    'date': ['2024-01-01', '2024-01-01', '2024-01-03', '2024-01-04']
}
df_bank = pd.DataFrame(data_bank)
# Convert date column to datetime and filter by month.
df_bank['date'] = pd.to_datetime(df_bank['date'])
# Group by acc_id → total deposited & withdrawn.
deposits = df_bank[df_bank['type'] == 'deposit'].groupby('acc_id')['amount'].sum()
withdrawals = df_bank[df_bank['type'] == 'withdraw'].groupby('acc_id')['amount'].sum()
# Identify accounts with more withdrawals than deposits.
more_withdraw = withdrawals > deposits
print("\nBank:")
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("More withdraw:", more_withdraw)
print("Jan trans:", df_bank[df_bank['date'].dt.month == 1])

# Hospital Patient Stay Duration
data_hosp = {
    "patient": ["A", "B", "C", "D"],
    "admission": ["2024-01-01", "2024-01-05", "2024-01-10", "2024-01-11"],
    "discharge": ["2024-01-07", "2024-01-12", "2024-01-14", "2024-01-18"]
}
df_hosp = pd.DataFrame(data_hosp)
# Convert dates to datetime type.
df_hosp['admission'] = pd.to_datetime(df_hosp['admission'])
df_hosp['discharge'] = pd.to_datetime(df_hosp['discharge'])
# Create a column = total hospital stay (days).
df_hosp['stay_days'] = (df_hosp['discharge'] - df_hosp['admission']).dt.days
# Which patient stayed longest?
longest = df_hosp.loc[df_hosp['stay_days'].idxmax(), 'patient']
# What is the average stay length?
avg_stay = df_hosp['stay_days'].mean()
print("\nHospital:")
print(df_hosp)
print("Longest stay:", longest)
print("Avg stay:", avg_stay)

# Delivery Order Dataset (Logistics)
df_del = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "distance_km": [2.5, 15, 9, 3, 20],
    "time_min": [12, 40, 25, 15, 55]
})
# Create new column = avg speed = distance_km / (time_min/60).
df_del['avg_speed'] = df_del['distance_km'] / (df_del['time_min'] / 60)
# Filter orders with avg speed < 20 km/h.
slow_orders = df_del[df_del['avg_speed'] < 20]
# Compute mean delivery speed.
mean_speed = df_del['avg_speed'].mean()
# Find the order with the fastest delivery.
fastest = df_del.loc[df_del['avg_speed'].idxmax(), 'order_id']
print("\nDelivery:")
print(df_del)
print("Slow orders:", slow_orders)
print("Mean speed:", mean_speed)
print("Fastest order:", fastest)
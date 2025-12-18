import tkinter as tk
from tkinter import messagebox

import mysql.connector

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",  # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="your_database"  # Replace with your database name
    )

# Create table if not exists
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            role VARCHAR(255),
            salary FLOAT
        )
    """)
    conn.commit()
    conn.close()

# CRUD Functions
def add_employee(name, age, role, salary):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, age, role, salary) VALUES (%s, %s, %s, %s)", (name, age, role, salary))
    conn.commit()
    conn.close()

def get_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_employee(emp_id, name, age, role, salary):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET name=%s, age=%s, role=%s, salary=%s WHERE id=%s", (name, age, role, salary, emp_id))
    conn.commit()
    conn.close()

def delete_employee(emp_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    conn.commit()
    conn.close()

# Tkinter GUI
class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee CRUD")
        
        # Labels and Entries
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Age:").grid(row=1, column=0)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1)
        
        tk.Label(root, text="Role:").grid(row=2, column=0)
        self.role_entry = tk.Entry(root)
        self.role_entry.grid(row=2, column=1)
        
        tk.Label(root, text="Salary:").grid(row=3, column=0)
        self.salary_entry = tk.Entry(root)
        self.salary_entry.grid(row=3, column=1)
        
        tk.Label(root, text="ID (for update/delete):").grid(row=4, column=0)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=4, column=1)
        
        # Buttons
        tk.Button(root, text="Add", command=self.add).grid(row=5, column=0)
        tk.Button(root, text="Update", command=self.update).grid(row=5, column=1)
        tk.Button(root, text="Delete", command=self.delete).grid(row=5, column=2)
        tk.Button(root, text="View All", command=self.view_all).grid(row=6, column=0, columnspan=3)
        
        # Listbox for display
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=7, column=0, columnspan=3)
        
        create_table()
    
    def add(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        role = self.role_entry.get()
        salary = float(self.salary_entry.get())
        add_employee(name, age, role, salary)
        messagebox.showinfo("Success", "Employee added")
        self.clear_entries()
    
    def update(self):
        emp_id = int(self.id_entry.get())
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        role = self.role_entry.get()
        salary = float(self.salary_entry.get())
        update_employee(emp_id, name, age, role, salary)
        messagebox.showinfo("Success", "Employee updated")
        self.clear_entries()
    
    def delete(self):
        emp_id = int(self.id_entry.get())
        delete_employee(emp_id)
        messagebox.showinfo("Success", "Employee deleted")
        self.clear_entries()
    
    def view_all(self):
        self.listbox.delete(0, tk.END)
        employees = get_employees()
        for emp in employees:
            self.listbox.insert(tk.END, f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Role: {emp[3]}, Salary: {emp[4]}")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.role_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()


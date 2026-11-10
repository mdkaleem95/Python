
# Program: Employee Information Management System

# Collect employee information
name = input("Enter Employee Name: ")
employee_id = int(input("Enter Employee ID: "))
age = int(input("Enter Employee Age: "))
salary = float(input("Enter Monthly Salary: "))
department = input("Enter Department: ")
is_active = True

# Calculate annual salary
annual_salary = salary * 12

# Display employee information
print("\n===== EMPLOYEE PROFILE =====")

print("Employee Name:", name)
print("Employee ID:", employee_id)
print("Age:", age)
print("Monthly Salary:", salary)
print("Annual Salary:", annual_salary)
print("Department:", department)
print("Active Employee:", is_active)

# Display data types
print("\n===== DATA TYPES =====")

print("Name:", type(name))
print("Employee ID:", type(employee_id))
print("Age:", type(age))
print("Salary:", type(salary))
print("Active Status:", type(is_active))

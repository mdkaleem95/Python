
# Program: Employee Salary Analysis System

# Employee records
employees = [
    {"name": "Kaleem", "salary": 110000},
    {"name": "Ali", "salary": 90000},
    {"name": "Ahmed", "salary": 75000},
    {"name": "Sara", "salary": 125000},
    {"name": "John", "salary": 60000}
]

total_salary = 0
high_salary_count = 0

print("===== EMPLOYEE SALARY REPORT =====")

# Process employee records
for employee in employees:

    name = employee["name"]
    salary = employee["salary"]

    annual_salary = salary * 12

    total_salary += salary

    print("\nEmployee:", name)
    print("Monthly Salary:", salary)
    print("Annual Salary:", annual_salary)

    # Identify high-earning employees
    if salary >= 100000:
        print("Category: High Earner")
        high_salary_count += 1
    else:
        print("Category: Regular Earner")

# Calculate average salary
employee_count = len(employees)
average_salary = total_salary / employee_count

print("\n===== SALARY SUMMARY =====")
print("Total Employees:", employee_count)
print("Total Monthly Salary:", total_salary)
print("Average Monthly Salary:", round(average_salary, 2))
print("High-Earning Employees:", high_salary_count)

# Demonstrate while loop
print("\n===== EMPLOYEE COUNTER =====")

counter = 1

while counter <= employee_count:
    print("Processed Employee:", counter)
    counter += 1

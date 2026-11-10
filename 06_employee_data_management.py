
# Program: Employee Data Management System

# 1. List - Store employee names
employees = ["Kaleem", "Ali", "Ahmed", "Sara", "John"]

print("===== EMPLOYEE LIST =====")

for employee in employees:
    print(employee)


# 2. Tuple - Store fixed employee details
employee_details = ("Kaleem", "Azure Data Engineer", 110000)

print("\n===== EMPLOYEE DETAILS =====")
print("Name:", employee_details[0])
print("Role:", employee_details[1])
print("Salary:", employee_details[2])


# 3. Set - Store unique departments
departments = {
    "Data Engineering",
    "DevOps",
    "HR",
    "Data Engineering"
}

print("\n===== UNIQUE DEPARTMENTS =====")
print(departments)


# 4. Dictionary - Store employee records
employee_records = {
    101: {
        "name": "Kaleem",
        "department": "Data Engineering",
        "salary": 110000
    },
    102: {
        "name": "Ali",
        "department": "DevOps",
        "salary": 90000
    },
    103: {
        "name": "Ahmed",
        "department": "Data Engineering",
        "salary": 85000
    },
    104: {
        "name": "Sara",
        "department": "HR",
        "salary": 75000
    }
}


# 5. Access dictionary records
print("\n===== EMPLOYEE RECORDS =====")

for emp_id, details in employee_records.items():

    print("Employee ID:", emp_id)
    print("Name:", details["name"])
    print("Department:", details["department"])
    print("Salary:", details["salary"])


# 6. Update employee salary
employee_records[101]["salary"] = 125000

print("\nUpdated Kaleem Salary:",
      employee_records[101]["salary"])


# 7. List slicing
print("\n===== FIRST THREE EMPLOYEES =====")
print(employees[:3])


# 8. List comprehension
high_salary_employees = [
    details["name"]
    for details in employee_records.values()
    if details["salary"] >= 90000
]

print("\n===== HIGH SALARY EMPLOYEES =====")
print(high_salary_employees)


# 9. Calculate total salary expense
total_salary = sum(
    details["salary"]
    for details in employee_records.values()
)

print("\nTotal Monthly Salary Expense:", total_salary)

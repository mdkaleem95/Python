
# Program: Employee File Management System

import csv
import os

# Custom Exception
class InvalidSalaryError(Exception):
    pass


# Employee records
employees = [
    {"id": 101, "name": "Kaleem", "department": "Data Engineering", "salary": 110000},
    {"id": 102, "name": "Ali", "department": "DevOps", "salary": 90000},
    {"id": 103, "name": "Ahmed", "department": "Data Engineering", "salary": 85000}
]

# Validate employee salary
def validate_salary(salary):

    if salary <= 0:
        raise InvalidSalaryError("Salary must be greater than zero.")

    return salary


# Write employee records to CSV
try:

    with open("employees.csv", "w", newline="") as file:

        fieldnames = ["id", "name", "department", "salary"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for employee in employees:

            validate_salary(employee["salary"])

            writer.writerow(employee)

    print("Employee records saved successfully.")

except InvalidSalaryError as error:
    print("Salary Validation Error:", error)

except PermissionError:
    print("Permission denied while writing the file.")

except OSError as error:
    print("File operation failed:", error)

finally:
    print("CSV writing operation completed.")


# Read employee records from CSV
try:

    with open("employees.csv", "r") as file:

        reader = csv.DictReader(file)

        print("\n===== EMPLOYEE RECORDS =====")

        for employee in reader:

            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])
            print("-------------------------")

except FileNotFoundError:
    print("Employee file does not exist.")

except PermissionError:
    print("Permission denied while reading the file.")


# Write summary to text file
try:

    with open("employee_summary.txt", "w") as file:

        file.write("EMPLOYEE MANAGEMENT SUMMARY\n")
        file.write("============================\n")

        file.write(f"Total Employees: {len(employees)}\n")

        total_salary = sum(
            employee["salary"] for employee in employees
        )

        file.write(f"Total Monthly Salary: {total_salary}\n")

    print("\nEmployee summary saved successfully.")

except OSError as error:
    print("Unable to write summary:", error)


# Display current working directory
print("\nCurrent Working Directory:", os.getcwd())

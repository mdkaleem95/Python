
# Program: Employee Payroll Management System

# Function to calculate annual salary
def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12


# Function to calculate bonus
def calculate_bonus(monthly_salary, bonus_percentage):
    return monthly_salary * bonus_percentage / 100


# Function to calculate tax deduction
def calculate_tax(annual_salary, tax_percentage):
    return annual_salary * tax_percentage / 100


# Function to generate employee payroll
def generate_payroll(name, department, monthly_salary):

    bonus_percentage = 10
    tax_percentage = 5

    annual_salary = calculate_annual_salary(monthly_salary)

    bonus = calculate_bonus(monthly_salary, bonus_percentage)

    tax = calculate_tax(annual_salary, tax_percentage)

    net_annual_salary = annual_salary + bonus - tax

    print("\n===== EMPLOYEE PAYROLL REPORT =====")

    print("Employee Name:", name)
    print("Department:", department)
    print("Monthly Salary:", monthly_salary)
    print("Annual Salary:", annual_salary)
    print("Annual Bonus:", bonus)
    print("Tax Deduction:", tax)
    print("Net Annual Salary:", net_annual_salary)

    return net_annual_salary


# Employee records
employees = [
    ("Kaleem", "Azure Data Engineering", 110000),
    ("Ali", "DevOps", 90000),
    ("Ahmed", "Data Engineering", 85000)
]

# Process payroll using a loop
total_payout = 0

for name, department, salary in employees:

    payout = generate_payroll(name, department, salary)

    total_payout += payout


# Lambda function to calculate salary category
salary_category = lambda salary: "High Salary" if salary >= 100000 else "Standard Salary"

print("\n===== SALARY CATEGORIES =====")

for name, department, salary in employees:
    print(name, ":", salary_category(salary))


# Display total payroll expense
print("\nTotal Annual Payroll Expense:", total_payout)

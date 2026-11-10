
# Program: Employee Management System using OOP


# Parent Class
class Employee:

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary  # Private attribute

    # Encapsulation - Getter method
    def get_salary(self):
        return self.__salary

    # Method to display employee details
    def display_details(self):
        print("\nEmployee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.__salary)

    # Method to calculate bonus
    def calculate_bonus(self):
        return self.__salary * 0.10


# Child Class - Developer
class Developer(Employee):

    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    # Method overriding - Polymorphism
    def display_details(self):
        super().display_details()
        print("Programming Language:", self.programming_language)

    def calculate_bonus(self):
        return self.get_salary() * 0.15


# Child Class - Data Engineer
class DataEngineer(Employee):

    def __init__(self, name, employee_id, salary, technology):
        super().__init__(name, employee_id, salary)
        self.technology = technology

    # Method overriding - Polymorphism
    def display_details(self):
        super().display_details()
        print("Technology:", self.technology)

    def calculate_bonus(self):
        return self.get_salary() * 0.20


# Create employee objects
employee1 = Developer(
    "Ali", 101, 90000, "Python"
)

employee2 = DataEngineer(
    "Kaleem", 102, 110000, "Azure Databricks"
)


# Store employees in a list
employees = [employee1, employee2]


# Display employee information
print("===== EMPLOYEE MANAGEMENT SYSTEM =====")

for employee in employees:

    employee.display_details()

    print("Annual Bonus:", employee.calculate_bonus())


# Display total employee count
print("\nTotal Employees:", len(employees))

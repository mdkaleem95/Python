pip install requests


# Program: API and JSON Data Extraction

import requests
import json

# Public REST API endpoint
API_URL = "https://jsonplaceholder.typicode.com/users"

# Function to fetch API data
def fetch_employee_data():

    try:

        response = requests.get(API_URL, timeout=10)

        # Check API response status
        response.raise_for_status()

        # Convert JSON response into Python data
        employee_data = response.json()

        return employee_data

    except requests.exceptions.Timeout:
        print("API request timed out.")

    except requests.exceptions.HTTPError as error:
        print("HTTP Error:", error)

    except requests.exceptions.RequestException as error:
        print("API Connection Error:", error)

    return []


# Function to process employee information
def process_employee_data(employees):

    print("\n===== API EMPLOYEE REPORT =====")

    for employee in employees:

        employee_id = employee["id"]
        name = employee["name"]
        email = employee["email"]
        company = employee["company"]["name"]

        print("\nEmployee ID:", employee_id)
        print("Name:", name)
        print("Email:", email)
        print("Company:", company)


# Function to save API response as JSON
def save_json_data(employees):

    try:

        with open("employees_api.json", "w") as file:

            json.dump(employees, file, indent=4)

        print("\nAPI data saved successfully.")

    except OSError as error:
        print("File saving error:", error)


# Main execution
if __name__ == "__main__":

    employees = fetch_employee_data()

    if employees:

        process_employee_data(employees)

        save_json_data(employees)

    else:
        print("No employee data available.")

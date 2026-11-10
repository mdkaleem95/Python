
# Program: Employee Performance Evaluation System

# Collect employee details
name = input("Enter Employee Name: ")
department = input("Enter Department: ")

# Collect performance scores
task_completion = float(input("Enter Task Completion Score (0-100): "))
quality_score = float(input("Enter Quality Score (0-100): "))
attendance_score = float(input("Enter Attendance Score (0-100): "))

# Calculate average performance score
average_score = (
    task_completion + quality_score + attendance_score
) / 3

# Determine performance rating
if average_score >= 90:
    rating = "Excellent"
elif average_score >= 75:
    rating = "Good"
elif average_score >= 60:
    rating = "Average"
else:
    rating = "Needs Improvement"

# Check bonus eligibility
if average_score >= 85 and attendance_score >= 90:
    bonus_status = "Eligible for Bonus"
else:
    bonus_status = "Not Eligible for Bonus"

# Display evaluation report
print("\n===== EMPLOYEE PERFORMANCE REPORT =====")

print("Employee Name:", name)
print("Department:", department)
print("Average Score:", round(average_score, 2))
print("Performance Rating:", rating)
print("Bonus Status:", bonus_status)

# Check whether employee meets minimum requirements
if average_score >= 60 or attendance_score >= 95:
    print("Status: Meets Performance Requirements")
else:
    print("Status: Below Performance Requirements")

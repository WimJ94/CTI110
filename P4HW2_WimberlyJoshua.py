# Joshua Wimberly
# 07/06/2025
# P4HW2 Assignment
# This program collects multiple employees' hours worked and pay rate, calculates their gross pay including regular and overtime pay.

# Pseudocode:
# 1. Initialize totals for regular pay, overtime pay, gross pay, and employee count.
# 2. Ask user for employee name.
# 3. While name is not "done":
#      Ask for hours worked and pay rate.
#      Calculate regular hours (up to 40) and overtime hours.
#      Calculate regular pay and overtime pay.
#      Calculate gross pay.
#      Display formatted results.
#      Update totals and increment employee count.
#      Ask for next employee name.
# 4. When "Done" is entered:
#      Display summary totals (total regular, overtime, gross pay, number of employees).

# Initialize totals
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

# Ask for first employee name
employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name != "Done":
    # Input data
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate regular and overtime hours
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(0, hours_worked - 40)

    # Calculate pays
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    # Display employee pay breakdown
    print("\n")
    print(f"Employee name: {employee_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<10}{'OT Pay':<12}{'Reg Pay':<12}{'Gross Pay':<12}")
    print("----------------------------------------------------------------------")
    print(f"{hours_worked:<15.2f}{pay_rate:<12.2f}{overtime_hours:<10.2f}{overtime_pay:<12.2f}{regular_pay:<12.2f}{gross_pay:<12.2f}")
    print("\n")

    # Update totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Prompt for next employee
    employee_name = input("Enter another employee's name or 'Done' to terminate: ")

# Display overall summary
print("\n")
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime   : ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular pay: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross       : ${total_gross_pay:.2f}")
print()

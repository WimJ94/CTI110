#Wimberly Joshua
# 6/26/2025
#P3HW2
# This program will take an employee's name,hours and pay rate and calculate the employee's pay.

# Gathers employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter pay rate: "))

print('----------------------------------')

# prints the employee's name
print(f'{"Employee's name:":>15}{employee_name:>15}')

#prints the employees hours worked, pay rate, overtime, overtime pay, regular hour pay and gross pay
print(f'{"Hours worked":>15}{"Pay Rate":>15}{"Overtime":>15}{"Overtime Pay":>15}{"RegHour Pay":>15}{"Gross Pay":>15}')

print('------------------------------------------------------------------------------------------')

# Calculate regular pay
 # Regular hours are capped at 40
regular_hours = min(hours_worked, 40) 
regular_pay = regular_hours * pay_rate

# Calculate overtime pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    overtime_pay = 0

#prints the Results
print(f'{hours_worked:>15.2f}{pay_rate:>12.2f}{overtime_hours:>15.2f}{overtime_pay:>15.2f}{regular_pay:>15.2f}{(regular_pay + overtime_pay):>15.2f}')

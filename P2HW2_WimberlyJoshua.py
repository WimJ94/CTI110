#WImberly Joshua
#6/19/2025
#P2HW2
#This program displays the grades for each module


#start o program
#declare variables and get user input for grades
module_1 = float(input("Enter the grade for Module 1: "))
module_2 = float(input("Enter the grade for Module 2: "))
module_3 = float(input("Enter the grade for Module 3: "))
module_4 = float(input("Enter the grade for Module 4: "))
module_5 = float(input("Enter the grade for Module 5: "))
module_6 = float(input("Enter the grade for Module 6: "))
#store the grades in a list
module_grades_list = [module_1, module_2, module_3, module_4, module_5, module_6]
#display the results section
print("------------Results------------")
#display the grades for each module
#using f-string to format the output
print(f"{'Lowest Grade:':<15}{min(module_grades_list):.2f}")
print(f"{'Highest Grade:':<15}{max(module_grades_list):.2f}")
print(f"{'Sum of Grades:':<15}{sum(module_grades_list):.2f}")
print(f"{'Average Grade:':<15}{sum(module_grades_list) / len(module_grades_list):.2f}")
print("---------------------------------------")
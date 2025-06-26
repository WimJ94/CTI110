# Wimberly Joshua
# 6/26/2025
# P3HW1
#debugging and testing code for grade caculations 
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
print('------------Results------------')


# TO DO: determine lowest, highest , sum and average for grades
lowest = min(grades)
highest = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / len(grades)

# prints lowest, highest, sum and average
print('Lowest grade is: ', lowest)
print('Highest grade is: ', highest)
print('Sum of grades is: ', sum_of_grades)
print('Average of grades is: ', average)

print('------------------------------')
# Display letter grade based on average
if average >= 90:
    print('Your Grade is: A')
elif average >= 80:
    print('Your Grade is: B')
elif average >= 70:
    print('Your Grade is: C')
elif average >= 60:
    print('Your Grade is: D')
else:
    print('Your Grade is: F') 

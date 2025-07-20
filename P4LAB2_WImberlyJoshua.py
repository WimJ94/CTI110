#Wimberly Joshua
#6/4/2025
#P4LAB2
#Uses for loop and while loop together
'''
Get interger from user
Determine if integer is positive or negative
if number is positive, display multiplication table
if number is negative, tell user program cannot accept it
ask user to run again?
if yes, run program
if no, close program
'''
run_again = "yes"
while run_again != "no":
user_num = int(input("Enter an integer: "))
if user_num >= 0:
for item in range(1, 13):
print(f"{user_num} * {item} = {user_num * item}")
else:
print("This program does not handle negative values")
run_again = input("Would you like to run the program again? ")
#End Loop
print("Program is ending")

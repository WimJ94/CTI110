#Wimberly Joshua
#06/12/2025
#P1HW1
# This program will take users input and caculate the results of different operations.

print("-----Caculating Exponenets-----\n")


base = input("Enter an integer as the base value: ")
expon = input("Enter an integer as the exponent: ")
final_value = int(base) * int(expon)
print()
print(base, "Rasied to the power of", expon, "is", final_value)


print("\n-----Addition and Subtraction-----\n")


start = input("enter a starting integer: ")
add = input("Enter an integer to add: ")
sub = input("Enter an integer to subtract: ")
value = int(start) + int(add) - int(sub)
print()
print(start, "+", add, "-", sub, "=", value)
# Wimberly Joshua
 # 6/12/2025
 # P1HW2
 # this program will calculate travel expenses


#Start
#Display "This program calculates and displays travel expenses"
print(" This program calculates and displays travel expenses  \n")
#Ask user to enter their total budget
#Store the answer in the var "budget"
budget = int(input("Enter Budget: "))
print()
#Ask user to enter their destination
#Store the answer in the var "destination"
destination = input("Enter Destination: ")
print()
#Ask user to enter how much they think they will spend on gas
#Store the answer in the var "gas"
gas = int(input("How much do you think you will spend on gas? "))
print()
#Ask user to enter how much they think they will spend on accomodation/hotel
#Store the answer in the var "hotel"
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
#Ask user to enter how much they think they will spend on food
#Store the answer in the var "food"
food = int(input("Last, how much do you need for food? "))  
#Display the "------------Travel Expenses------------"
print("\n------------Travel Expenses------------\n")
#Display the destination, budget, gas, hotel, food, and total spent
print("Location: ", destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)
#add the gas, hotel, and food to get the total spent
total_spent = gas + hotel + food  
#subtract the total spent from the budget
total = budget - total_spent
print()
#Display the total spent
print("Remaining Balance: ", total)


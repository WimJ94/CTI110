#Wimberly Joshua
#07/10/2025
#P5LAB
#using user-defined functions

import random

def disperse_change(change):
        #converts to integer
        my_money = int(change * 100)

        # determines how much change is needed
        num_dollars = my_money // 100
        my_money = my_money - (num_dollars * 100)

        num_quarters = my_money // 25
        my_money = my_money - (num_quarters * 25)

        num_dimes = my_money // 10
        my_money = my_money - (num_dimes * 10)

        num_nickels = my_money // 5
        my_money = my_money - (num_nickels * 5)

        num_pennies = my_money
        my_money = my_money - (num_pennies * 1)

        # if statements that determine what to print out
        if num_dollars > 0:
            if num_dollars == 1:
                print(f"{num_dollars} Dollar")
            else:
                print(f"{num_dollars} Dollars")
        if num_quarters > 0:
            if num_quarters == 1:
                print(f"{num_quarters} Quarter")
            else:
                print(f"{num_quarters} Quarters")
        if num_dimes > 0:
            if num_dimes == 1:
                print(f"{num_dimes} Dime")
            else:
                print(f"{num_dimes} Dimes")
        if num_nickels > 0:
            if num_nickels == 1:
                print(f"{num_nickels} Nickel")
            else:
                print(f"{num_nickels} Nickels")
        if num_pennies > 0:
            if num_pennies == 1:
                print(f"{num_pennies} Penny")
            else:
                print(f"{num_pennies} Pennies")

        
              
    


def main():
    #logic goes here

    #generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")


    #var represents money put in the machine
    money_in = float(input("How mouch cash will you put in the self checkout?"))

    #change owed to customer
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    disperse_change(change)




#call the main function
main()

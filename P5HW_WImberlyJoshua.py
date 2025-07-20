#Wimberly Joshua
#7/10/2025
#P5HW
#this program is a short game called door of fate

import random

def create_player():
    #returns the player stats as a dictionary
    return{"score": 0, "status": "alive"}

def get_door_outcome():
    #randomly returns outcome as a string
    return random.choice(["Gold", "Death", "Extra Point"])

def play_round(player, round_num):
    #runs one round of the game and updates the players dictionary
    print(f"\n Round {round_num}")
    print("Choose a door that speaks to your soul!!(1, 2, or 3)")

    try:
        choice = int(input("Enter the door of your choosing: "))
        if choice not in [1, 2, 3]:
            print("Invalid door choice are you scared of your fate? You lose your turn!")
            return
        
        outcome = get_door_outcome()

        if outcome == "Gold":
            print("You found a bag of gold! Wealth to you my friend! +1 Point")
            player["score"] += 1
        elif outcome == ("Death"):
            print("Oh No!!! You have met your doom at Death's door!")
            player["status"] = "Dead"
        elif outcome == "Extra Point":
            print("You've earned an Extra Point! Lady Luck is on your side! + 2 Points")
            player["score"] += 2

    except ValueError:
        print("The gods were not happy this time!, turn skipped!")

def main():
    while True:
        print("\n===============================")
        print("🎭 WELCOME TO THE DOOR OF FATE 🎭")
        print("===============================\n")
        print("You have 5 rounds to become the richest ruler 👑")
        print("Or meet your doom at the hands of fate! 💀\n")
        print("There are 3 mysterious doors: 🚪1 🚪2 🚪3\n")

        player = create_player()

        for round_num in range(1, 6):
            if player["status"] == "Dead":
                print("\n Game Over! You have fallen to your fate!")
                break
            play_round(player, round_num)

        print("\n🎉 Game Complete!")
        print(f"Final Score: {player['score']} ⭐")
        if player["status"] == "alive":
            print("You have survived your own fate! Take your Riches and have an ale on me! 🎊")
        else:
            print("Fate is a cruel mistress....")

        play_again = input("Would you like to temp your fate again travler? yes or no? ")
        if play_again != "yes":
            print("Thanks for playing! Goodbye travler!")
            break


if __name__ == "__main__":
    main()            



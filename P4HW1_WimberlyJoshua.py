# Josh Wimberly
# 2025-07-06
# P4HW1 Assignment
# This program asks the user how many test scores they want to enter and caculates the grade

# Pseudocode:
# Ask user how many scores they want to enter
# Create empty list to store scores
# Loop until all scores are collected:
#     Ask for score
#     If score is not between 0 and 100:
#         Display error message and ask again
#     Else:
#         Add to score list
# After all scores are collected:
#     Find and display lowest score
#     Remove the lowest score from the list
#     Display modified score list
#     Calculate and display average of remaining scores
#     Display letter grade based on average


# Ask user how many scores to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create list to store valid scores
score_list = []

# Loop to collect scores
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i+1}: "))
        if 0 <= score <= 100:
            score_list.append(score)
            break
        else:
            print("INVALID score entered!!!!")
            print("Score should be between 0 and 100")

# Process the list
lowest_score = min(score_list)
score_list.remove(lowest_score)

average_score = sum(score_list) / len(score_list)

# Display results
print("\n----------Results----------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average_score:.2f}")

# Determine and display letter grade
if average_score >= 90:
    print("Grade         : A")
elif average_score >= 80:
    print("Grade         : B")
elif average_score >= 70:
    print("Grade         : C")
elif average_score >= 60:
    print("Grade         : D")
else:
    print("Grade         : F")

print("--------------------------")
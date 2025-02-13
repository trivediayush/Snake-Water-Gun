import random

# Map choices to meaningful names
choices = {-1: "Snake", 1: "Water", 0: "Gun"}
# Reverse mapping for user input
user_mapping = {"s": -1, "w": 1, "g": 0}

# Computer makes a random choice
computer = random.choice([-1, 1, 0])

# Get user's choice
user_input = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Validate user input
if user_input not in user_mapping:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    # Map user input to game choice
    you = user_mapping[user_input]

    print(f"You chose {choices[you]}")
    print(f"Computer chose {choices[computer]}")

    # Determine the winner
    if computer == you:
        print("It's a draw!")
    elif (you == -1 and computer == 1) or (you == 1 and computer == 0) or (you == 0 and computer == -1):
        print("You win!")
    else:
        print("You lose!")

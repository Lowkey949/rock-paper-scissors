import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice not in options:
        print("Invalid input. Please try again.")
        continue

    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        print("You win!" if computer_choice == "scissors" else "You lose!")
    elif user_choice == "paper":
        print("You win!" if computer_choice == "rock" else "You lose!")
    elif user_choice == "scissors":
        print("You win!" if computer_choice == "paper" else "You lose!")

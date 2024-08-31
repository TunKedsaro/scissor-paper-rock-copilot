# Import the random module
import random

# Create a list of option that has rock, paper, and scissors
options = ["rock", "paper", "scissors"]

# create a variable that will keep track of the number of wins, losses, and ties
options = ["rock", "paper", "scissors"]

# create a score variable and set it to 0
score = 0

# create a variable to count the number of rounds
round = 0

# create a while loop that loops
while True:
    # create a variable that stores the user's choice
    user_choice = input("Enter rock, paper, or scissors: ")

    # create a variable that stores the computer's choice (randomly generated)
    computer_choice = random.choice(options)

    # if the user's choice is rock
    if user_choice == "rock":
        # add the rounds variable by 1
        round += 1
        # if the computer's choice is rock
        if computer_choice == "rock":
            print("It's a tie!")
        # if the computer's choice is paper
        elif computer_choice == "paper":
            print("You lose!")
            score -= 1
        # if the computer's choice is scissors
        elif computer_choice == "scissors":
            print("You win!")
            score += 1

    # if the user's choice is paper
    elif user_choice == "paper":
        round += 1
        # if the computer's choice is rock
        if computer_choice == "rock":
            # print out "You win!"
            print("You win!")
            # increment the score variable
            score += 1
        # if the computer's choice is paper
        elif computer_choice == "paper":
            # print out "It's a tie!"
            print("It's a tie!")
        # if the computer's choice is scissors
        elif computer_choice == "scissors":
            # print out "You lose!" 
            print("You lose!")
            score -= 1

    elif user_choice == "scissors":
        # add the rounds variable by 1
        round += 1
        # if the computer's choice is rock
        if computer_choice == "rock":
            # print out "You lose!"
            print("You lose!")
            # if the computer's choice is paper
            score -= 1
        elif computer_choice == "paper":
            # print out "You win!"
            print("You win!")
            # increment the score variable
            score += 1
        # if the computer's choice is scissors
        elif computer_choice == "scissors":
            # print out "It's a tie!"
            print("It's a tie!")
    
    # if the user enter something other than rock, paper, or scissors
    else:
        # print out "Invalid choice!"
        print("Invalid choice!")

    # ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")

    # if the user enters "n"
    # break out of the while loop
    # print out the score and the number of rounds
    if play_again == "n":
        break
    else:
        print("Score: "+ str(score))
        print("Number of rounds: "+ str(round))

    if play_again == "y":
        continue



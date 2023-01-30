# import the 'random' module
import random

def start_game():

    # generate a random number between 1 and 100 (inclusive)
    secret_num = random.randint(1, 100)

    # initialize a variable to store the number of guesses the player has made
    guesses_made = 0

    # set the maximum number of allowed guesses
    max_guesses = 10

    # print a welcome message
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")


    # create a 'while' loop that continues until the player guesses the secret number or exceeds the maximum number of allowed guesses
    while guesses_made < max_guesses:
        # prompt the player to enter their guess
        guess = int(input("Enter your guess: "))

        # increment the number of guesses the player has made
        guesses_made += 1

        # check if the player's guess is less than the secret number
        if guess < secret_num:
            print("Your guess is too low. Try again.")
        # check if the player's guess is greater than the secret number
        elif guess > secret_num:
            print("Your guess is too high. Try again.")
        # if the player's guess is neither less than nor greater than the secret number, it must be equal to the secret number
        else:
            # print a message indicating that the player has won the game
            print("Congratulations! You guessed the secret number in {} guesses!".format(guesses_made))
            # exit the loop
            break

    # if the player has exceeded the maximum number of allowed guesses, print a message indicating that they have lost the game
    if guesses_made == max_guesses:
        print("Sorry, you have exceeded the maximum number of allowed guesses. The secret number was {}.".format(secret_num))

# start the first game
start_game()

# ask the player if they want to play again
play_again = input("Would you like to play again? Enter 'yes' or 'no': ")

# if the player wants to play again, start a new game
if play_again.lower() == 'yes':
    start_game()

# if the player does not want to play again, print a goodbye message
else:
    print("Thank you for playing! Goodbye.")
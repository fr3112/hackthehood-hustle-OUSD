# Guessingg game -Erika, Emari, Aiden
import random

def generate_random_number():
    return random.randint(1, 100) #This returns the random number that  is generated

def get_user_guess():
    user_try = False
    while user_try == False:
        guess_number = int(input("Put your guess number: ")) #Starts the game by asking you to put your guessing number

        if not type(guess_number) is int:
            raise ValueError("The number is not an integer")
        elif guess_number < 1 or guess_number > 100:
            print("The number is not in the range") #To make sure the number is within the range
        else:
            return guess_number

def play_guessing_game(): #It is  the main  function of the game that implements the two helper functions
    secret_number = generate_random_number()
    
    user_input = False
    tries = 0
    while user_input == False: #This help the game_loop function
        user_number = get_user_guess()
        tries += 1

        if user_number == secret_number: #This compares the number that the user puts with the secret number
            print("You are correct!")
            user_input = True
        elif user_number < secret_number:
            print("You are too low")
        else:
            print("You are too high")

        print(f"Your # of tries: {tries}") #This print the number of tries
        print("If you want to leave put \'E\'")
    return user_input
    
    
def game_loop(): #This does a loop that can finish only if the user puts the correct number
    user_tries = False
    while user_tries == False: #If the user is not correct it runs the play guessing ggame again
        user_tries = play_guessing_game()

if __name__ == "__main__": #This run the game
    game_loop()

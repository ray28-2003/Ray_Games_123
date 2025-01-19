import random

def number_guessing_game():
    lower_bound = 1
    upper_bound = 100

    number_to_guess = random.randint(lower_bound,upper_bound)
    attempts =25
    print(f"welcome to the number guessing game!")
    print(f"i'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"you have{attempts} attempts to guess the correct number.")

    while attempts > 0:
        try:

            guess = int(input(f"guess the number({attempts} attempts left):"))

            if guess == 0:
                print("End of the game.")
                print(f"The number is {number_to_guess}.")
                break

            if guess == number_to_guess:
                print(f"congratulation! you've guessed the number {number_to_guess}")
                break
            elif guess < number_to_guess:
                print("Too low! try a higher number.")
            else:
                print("too high! try a lower number.")

            attempts -=1
        except ValueError:
            print("invalid input! please enter a valid number.")

    if attempts == 0:
        
        print(f"sorry, you've run out of attempts. the correct number was {number_to_guess}.")

number_guessing_game() 

    
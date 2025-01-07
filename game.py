import random

def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def get_user_choice():
    while True:
        user_choice = input("enter rock paper or scissors:").lower()
        if user_choice in ['rock','paper','scissors']:
            return user_choice
        else:
            print("invalid input, please choose rock, paper or scissors.")

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "it's a tie!"
    elif(user_choice == 'rock' and computer_choice =='scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper')or\
        ( user_choice == 'paper' and computer_choice =='rock'):
       return "you win!"
    else:
        return "computer wins!"
    
def play_game():
    print("welcome to rock,paper,scissors!")

    user_choice =get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nyou chose: {user_choice}")
    print(f"computer choose: {computer_choice}")
    result = determine_winner(user_choice,computer_choice)
    print(result)

if __name__ =="__main__":
    play_game()

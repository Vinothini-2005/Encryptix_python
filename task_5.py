import random

def userChoice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose Rock, Paper, or Scissors:").lower()
    while user_choice not in choices:
        print("Invalid choices....Please enter a valid choice")
        user_choice = input("Choose Rock, Paper, or Scissors:").lower()
    return user_choice

def botChoice():
    return random.choice(['rock', 'paper', 'scissors'])

def selectWinner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "tie"
    elif (user_choice == "rock" and bot_choice == "scissors") or(user_choice == "scissors" and bot_choice == "paper") or (user_choice == "paper" and bot_choice == "rock"):
        return "user"
    else:
        return "bot"

def resultDisplay(user_choice, bot_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Bot chose: {bot_choice}")
    if winner == "tie":
        print("It's TIE")
    elif winner == "user":
        print("Well Done!....You WIN")
    else:
        print("Oops....You LOSE")

def playAgain():
    return input("\nDo you want to play again (yes / no)?:").lower().startswith('y')

def playing():
    user_score = 0
    bot_score = 0
    while True:
        user_choice = userChoice()
        bot_choice = botChoice()
        winner  = selectWinner(user_choice, bot_choice)
        resultDisplay(user_choice, bot_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "bot":
            bot_score += 1

        print(f"\nScore \nYou: {user_score} \nBot: {bot_score}")

        if not playAgain():
            break

    print("Thanks for playing!...")



rps = playing()
    
    
    

import random

print("Welcome to the ultimate game: ROCK - PAPER - SCISSORS")


def whoWon(user, computer):
    if ((user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p")):
        return True
    return False
   
playing = True

while playing:  
    cond = input("\nPlease type 't' to continue playing else type 'f': ")
    if cond == "t":
        playing = True
    else:
        playing = False
        break
    user = input("What's your call: 'r' for rock, 'p' for paper, and 's' for scissors' -  ")
    possibilities = ['r', 'p', 's']
    if user not in possibilities:
        print("Please choose between 'r', 'p', or 's' for rock, paper or scissors respectively")
        continue
    computer = random.choice(possibilities)
    if computer == "r":
        print("I chose rock as my call!")
    elif computer == "p":
        print("I chose paper as my call!")
    else:
        print("I chose scissors as my call!")
    
    if user == computer:
        print("It's a tie. Nice, give it another try!")
    else:
        if whoWon(user, computer):
            print("Whooray, you WON! Well played.")
        else:
            print("Better luck next time! You lost.")

print("Thank you for playing! Hope you had fun")

import random
win = 0
loss = 0
draw = 0

def getUserChoice():
    while True:
        userChoice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if userChoice in ("rock", "paper", "scissors"):
            return userChoice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def getComputerChoice():
    return random.choice(["rock", "paper", "scissors","sissors", "paper", "rock"])

def winner(userChoice, computerChoice):
    global win, loss, draw
    if computerChoice == "rock" and userChoice == "paper":
        print("PAPER covers the ROCK. You Win.")
        win += 1
    elif computerChoice == "rock" and userChoice == "scissors":
        print("ROCK breaks the SCISSORS. You Lose.")
        loss += 1
    elif computerChoice == "paper" and userChoice == "rock":
        print("PAPER covers the ROCK. You Lose.")
        loss += 1
    elif computerChoice == "paper" and userChoice == "scissors":
        print("SCISSORS cuts the PAPER. You Win.")
        win += 1
    elif computerChoice == "scissors" and userChoice == "rock":
        print("ROCK breaks the SCISSORS. You Win.")
        win += 1
    elif computerChoice == "scissors" and userChoice == "paper":
        print("SCISSORS cuts the PAPER. You Lose.")
        loss += 1
    else:
        print("\nWe picked the same thing. This round is a Draw.")
        draw += 1

def main():
    global win, loss, draw
    print("Welcome to ROCK PAPER SCISSORS GAME.The computer will be your opponent.")
    userName = input("Enter your name: ")
    print(f"Welcome {userName} ")
    while True:
        userChoice = getUserChoice()
        computerChoice = getComputerChoice()
        print(f"{userName}, you chose {userChoice}. Computer chose {computerChoice}")
        result = winner(userChoice, computerChoice)
        print(f"Your score: {win}, Computer's score: {loss}, Games drawn: {draw}")
        again = input("If you want to play another round  Enter \"yes\".").strip().lower()
        if again != "yes":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()

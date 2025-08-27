import random

def win(user, computer):
    return (
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock") or
        (user == "rock" and computer == "scissors")
    )

def play():
    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("Choose rock, paper, or scissors: ").lower()

        if user not in choices:
            print("Invalid choice! Please type rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie! Rematch...")
            continue
        elif win(user, computer):
            print("You win!")
        else:
            print("You lose!")
        break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    play()

    while True:
        again = input("Play again? (yes/no): ").lower()
        if again == "yes":
            play()
        else:
            print("Thanks for playing! Goodbye.")
            break



  

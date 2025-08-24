import random
def play():
  user=input("Choose anyone rock,paper,scissors :: ").lower()
  choices=["rock","paper","scissors"]
  if user not in choices:
     return "Wrong input please give valid input"
  
  computer=random.choice(choices)
  print(f"computer choice:{computer}")

  if user==computer:
     return "Its Tie "
  if win(user,computer):
     return "You are win:"
  else:
     return "You Lose Try again:"     

def win(user,computer):
   return ((user=="scissors" and computer=="paper")or
           (user=="paper"and computer=="rock")or
           (user=="rock"and computer=="scissors"))

while True:
    print(play())
    again=input("If you want to play::(Yes/No)").lower()
    if again!="yes":
        print("Thanks for Playing")
        break
      


  
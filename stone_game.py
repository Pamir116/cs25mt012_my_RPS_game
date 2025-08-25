print("Rock, Paper, Scissors (also known by several other names and word orders) is an intransitive hand game, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist: ✊), "paper" (a flat hand: ✋), and "scissors" (a fist with the index finger and middle finger extended, forming a V: ✌️). The earliest form of a "rock paper scissors"-style game originated in China and was subsequently imported into Japan, where it reached its modern standardized form, before being spread throughout the world in the early 20th century.[citation needed]A simultaneous, zero-sum game, it has three possible outcomes: a draw, a win, or a loss. A player who decides to play rock will beat another player who chooses scissors ("rock crushes scissors" or "breaks scissors" or sometimes "blunts scissors"[1]), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same shape, the game is tied, but is usually replayed until there is a winner.Rock paper scissors is often used as a fair choosing method betwee")


import random   

def win(user,computer):
   return ((user=="scissors" and computer=="paper")or
           (user=="paper"and computer=="rock")or
           (user=="rock"and computer=="scissors"))


      


  

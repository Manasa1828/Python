#rock paper scissor game 
from random import randint
choice=['rock','scissor','paper']
user=input(f"choose from {choice}")
computer=choice[randint(0,2)]
print(computer)
if user==computer:
    print("DRAW MATCH")
elif user== "paper" and computer=="rock":
    print("user 1 wins")
elif user== "rock" and computer=="scissor":
    print("user 1 wins")
elif user== "scissor" and computer=="paper":
    print("user 1 wins")
else:
    print("computer 1 wins")

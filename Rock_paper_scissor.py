#rock paper scissor game with some limits

from random import randint
n=int(input("enter a number of turns:"))
choice=['rock','scissor','paper']
sum=0
count=0
for i in range(n):
    user=input(f"choose from {choice}")
    computer=choice[randint(0,2)]
    print(computer)
    if user==computer:
        print("DRAW MATCH")
    elif user== "paper" and computer=="rock":
        print("user 1 wins")
        sum=sum+1
    elif user== "rock" and computer=="scissor":
        print("user 1 wins")
        sum=sum+1
    elif user== "scissor" and computer=="paper":
        print("user 1 wins")
        sum=sum+1
    else:
        print("computer 1 wins")
        count+=1
print("user score:",sum)
print("computer score:",count)
if sum>count:
    print("User 1 wins")
else:
    print("computer wins")
    
    

"""
#Guess the secret number from the user
secret_number = 9
guess_count=0
guess_limit = 3
while guess_count<guess_limit:
    guess = int(input('Guess:'))
    guess_count +=1
    if guess == secret_number:
        print('you won!')
        break
else:
    print('Sorry , you failed!')
"""


"""
#car game
command = ""
started = False
while True:
    command = input(">").lower()
    if command == 'start':
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started...")
    elif command == 'stop':
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print("car stopped.")
    elif command == 'help':
        print("""
"""start - to start the car
stop - to stop the car
quit - to quit"""
""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand what your saying")
"""



"""#For loops
for i in ['MANASA', 'MANISHA', 'MAHI']:
    print(i)"""

"""
for i in range(5,10,2):
    print(i)
"""
"""
for i in range(2,7,4):
    print(i)
"""

"""
for i in range(1,10,3):
    print(i)
"""

"""
prices = [10,20,30]
total=0
for price in prices:
    total +=price
print(f"Total: {total}")
"""

""
#nested loops
for x in range(4):
    for y in range(3):
       print(f"({x}, {y})")

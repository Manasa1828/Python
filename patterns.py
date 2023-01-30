"""patterns

1. basic patterns
2. mirror image pattern
3. symmetrical pattern
4. choice pattern
5. anti- pattern/hallow pattern----- square, traingle,rightangle traiangle"""

"""rows=int(input("enter number of rows"))
for i in range(rows):
    for j in range(i+1):
        print(j+1 , end=" ")
    print('\n')



rows=int(input("enter number of rows"))
for i in range(rows):
    for j in range(i+1):
        print("$" , end=" ")
    print('\n')



rows=int(input("enter number of rows"))
for i in range(rows):
    for j in range(i+1):
        print(i , end=" ")
    print('\n')
"""

#inverted traingle  number analysis
"""rows=int(input("enter number of rows"))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(j+1 , end=" ")
    print('\n')"""

    
rows=5
for i in range(rows):
    for j in range(i+1):
        print(j+1 , end=" ")
    print('\n')

rows=5
for i in range(0,rows+1):
    for j in range(0,rows):
        if(j<i):
            print(' ', end=" ")
        else:
            print(j+1, end=" ")
    print('\n')


"""rows=5
for i in range(rows):
    for j in range(i+1):
        print(j+1 , end=" ")
    print('\n')"""



rows=5
for i in range(0,rows+1):
    for j in range(0,rows+1):
        if(j<i):
            print(' ', end=" ")
        else:
            print(j+1, end=" ")
    print('\n')

"""rows=int(input("enter a number"))
for i in range(0,rows+1):
    for j in range(0,rows):
        if(j<i):
            print(' ', end=" ")
        else:
            print(j+1, end=" ")
    print('\n')"""

"""rows=int(input("enter number of rows"))
for i in range(rows):
    for j in range(i+1):
       print("$" , end=" ")
    print('\n')"""

'''#mirror image of lower value 4 sides

rows=6 # leftside
for i in range(0,rows):
    for j in range(rows,0,-1):
        if(j>i):
            print(' ', end=" ")
        else:
            print(j+1, end=" ")
    print('\n')

rows=6  # right side
for i in range(rows):
    for j in range(i+1):
       print(j+1 , end=" ")
    print('\n')
    
rows=6 # down left side 
for i in range(0,rows+1):
    for j in range(0,rows):
        if(j<i):
            print(' ', end=" ")
        else:
            print(j+1, end=" ")
    print('\n')

rows=6 # down right side
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(j+1 , end=" ")
    print('\n')'''



"""#equilateral traingle
rows=5
for i in range(0,rows+1):
    for j in range(0,rows):
        if(j<i):
            print('', end=" ")
        else:
            print("*", end=" ")
    print('\n')"""


"""rows=6
for i in range(rows):
    for j in range(i+1):
        print(j+1, end = " ")
    print("\n")"""

"""#diamond or rhombus pattern using while loop
rows=6
i =1
while i<=rows:
    j= rows
    while j>i:
        print(' ', end=' ')
        j-=1
    print('*',end=" ")
    k=1
    while k<2 *(i-1):
        print(' ', end= ' ')
        k+=1
    if i==1:
        print()
    else:
        print('*')
    i+=1
i=rows -1
while i>=1:
    j=rows
    while j>i:
        print(' ',end=' ')
        j-=1
    print('*',end=' ')
    k=1
    while k<2 *(i-1):
        print(' ', end= " ")
        k+=1
    if i==1:
        print()
    else:
        print('*')
    i-=1"""


#diamond or rhombous using for loop

rows=6
k=2*rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
k= rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")



word = "california"
x=""
for i in word:
    x+=i
    print(x)
    

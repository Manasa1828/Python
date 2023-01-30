"""word= "india"
x=""
for i in word:
    x+=i
    print(x)"""



a = 39
r = 11
for i in range(0,r):
    for j in range(0,i+1):
        ch= chr(a)
        print(ch,end=' ')
        a+=1
    print(" ")


"""a = 65
r = 11
for i in range(0,r):
    for j in range(0,i+1):
        ch= chr(a)
        print(ch,end=' ')
        a+=1
    print(" ")"""


"""#equilateral traingle
a = 97
r = 5
k = (2*a)-2
for i in range(0,r):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        ch= chr(a)
        print(ch,end=' ')
        a+=1
    print(" ")

a = 65
r = 5
k = (2*a)-2
for i in range(0,r):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        ch= chr(a)
        print(ch,end=' ')
        a+=1
    print(" ")"""

"""#multiplication table left side
rows=int(input("enter number of rows"))
for i in range (1,rows+1):
    for j in range(1, i+1):
       print(i*j, end=" ")
    print()

rows=int(input("enter number of rows"))
for i in range (1,rows+1):
    for j in range(1, i+1):
       print(i-j, end=" ")
    print()

rows=int(input("enter number of rows"))
for i in range (1,rows+1):
    for j in range(1, i+1):
       print(i+j, end=" ")
    print()  """


#'''def username (arg1, arg2..
     #----
      #--
      #return 

def diff(a,b):
    return a-b
x=20
y=10
operation=diff
print(operation(x,y))

def diff(a,b):
    return a*b
x=20
y=10
operation=diff
print(operation(x,y))
            
def diff(a,b):
    return a+b
x=20
y=10
operation=diff
print(operation(x,y))



            

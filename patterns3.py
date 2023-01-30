"""def fun():
    for i in range(5):
        print("Hello this is Manasa")
fun()


def Mul(a,b):
    result = a*b
    print("Mul of a&b is ", result)
a=20
b=10
Mul(a,b)



def fun():
    print("abd")
    for i in range(5):
        print("Hello")
fun()
"""


"""blue bandit wants the list of prime numbers available in a range of numbers
   input 1 should be lessed than input 2 both the inputs should be positive
   range must always be greater than zero.
   use only for loop and one while loop
   sample input:1
   2
   15
   output 1 : 2 3 5 7 11 13  """
   
a=int(input("enter a first number"))
b=int(input("enter a last number"))
if(a<=0 or b<=0 or a>b):
    print("invalid input")
else:
   while (a<=b):
      if(a==2):
        print( end=" ")
      elif(a==1):
         a+=1
         continue
      else:
        flag=0
        for i in range(2,a//2+1):
            if a%i==0:
                flag=1
                break
        if flag==0:
            print(a,end=" ")
        a+=1
   

"""#plus pattern
n=int(input("enter a number"))
val=n * 2 -1
for i in range(1,2*n):
    for j in range(1,2*n):
        if i==n or j==n:
           print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#x pattern
n=int(input("enter a number"))
val=n * 2 -1
for i in range(1,2*n):
    for j in range(1,2*n):
        if i==j or j==val-i+1:
           print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#another method for plus
n=int(input("enter a number"))
val=n * 2 -1
for i in range(1,val+1):
    for j in range(1,val+1):
        if i==n or j==n:
           print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""

#sand glass pattern
n=int(input("enter a number"))
val = 0
st = int(n/2+1)
if n%2!=0:
    for i in range(1, int(n/2+2)):
        for j in range(1, val+1):
            print(' ',end=' ')
        for k in range(1,st+1):
            print('*',end=' ')
        print()
        val+=1
        st-=1
    val-=2
    st+=2
    for i in range(int(n/2+2),n+1):
       for j in range(1,val+1):
          print(' ', end=' ')
       for k in range(1,st+1):
          print('*',end=" ")
       print()
       val=-1
       st+=1
else:
    print("provide accurate input")
    


    

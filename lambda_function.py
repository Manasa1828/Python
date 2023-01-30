#lambda function
#many inputs and we will get only one output
"""properties of lambda
1.lambda fun have no predefined names
2. It can take n number of attributes
3. it can only return 1 value
4. lambda fun cannot access global variable
5. cannot access variable other than their parameters list
6. cannot contain multi parameters
7. It does not have explict return statements"""




"""Mul = lambda a,b,c:a*b*c
print("sum=",Mul(10,20,40))

add= lambda a,b,c:a+b+c
print("sum=",add(10,20,40))"""

#program to find samller number by lambda
"""def small(a,b):
    if(a<b):
        return a
    else:
        return b
add = lambda x,y: x+y
diff = lambda x,y:x-y
print("smaller of two no.", small(add(-3,-2),diff(-1,8)))"""


"""def increment(y):
    return (lambda x : x+1)(y)
a=100
print("a=", a)
print("a after incrementing")
b= increment(a)
print(b) """       




"""def fun(f, n):
    print(f(n))
twice = lambda x:x*2
triple = lambda x:x*3
fun(twice,4)
fun(triple,5)"""


"""x= lambda : sum(range(1,11))
print(x())"""

"""def swapfun(a,b):
     a=a+b
     b=a-b
     a=a-b
     print("after swap x:",a," and y:",b)
x=4
y=7
print("before swap x:",x," and y:",y)
swapfun(x,y)"""


"""def name(fn, ln):
    s=' '
    n= fn+s+ln
    return n
print(name("Manasa", "Gandamalla"))"""

"""def EvenOdd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
n=int(input("enter a number"))
EvenOdd(n)"""

#write a program to calculate SI, suppose the customer is a senior citizen. he is being offered 12% ROI;for all other customer, the ROI is 10%
"""def SI(p,r,ROI):
    si=p*r*ROI/100
    print(si)
def CI(p,r,ROI2):
    ci=p*r*ROI2/100
    print(ci)
pi=200
ri=3
ROI=10
ROI2=12
SI(pi,ri,ROI)
CI(pi,ri,ROI2)"""


"""p=200
r=3
si = p X r X ROI/100"""


"""#factorial program

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number"))
print(fact(n))"""


#program to find the exp(x,y) using recurssion function

"""def exp(x,y):
    if(y==0):
        return 1
    else:
        return(x*exp(x,y-1))
n=int(input("enter a number"))
m=int(input("enter a number"))
print("result=",exp(n,m))"""

"""def fib(n):
    if n<2:
        return 1
    return (fib(n-1)+fib(n-2))
n=int(input("enter a number"))
for i in range(n):
   print("Element(",i,")=",fib(i))"""




    
    
"""#Tower of Hanio
def H_Tower(n,A,B,C):
    if n>0:
        H_Tower(n-1,A,C,B)
        if A:
            C.append(A.pop())
        H_Tower(n-1,B,A,C)
A=[1,2,3,4]
B=[]
C=[]
print(A,B,C)
H_Tower(len(A),A,B,C)
print(A,B,C)"""
            

#check if two strings match where one string contains wildcard characters

"""def solve(a,b):
    n,m,=len(a),len(b)
    if n==0 and m==0:
        return True
    if n>1 and a[0] =='*' and m==0:
        return False
    if(n>1 and a[0] == '?')or(n!=0 and m!=0 and a[0] == b[0]):
        return solve(a[1:],b[1:])
    if n!=0 and a[0] =='*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False
x=str(input("enter the string with char"))
y=str(input("enter the string for match"))
print("with wild characters:",x)
print("without wild characters::",y)
print(solve(x,y))"""


"""n=50
a=0
b=1
count=0
if n<=0:
    print("enter positive number")
elif n==1:
    print("Fibonacci series upto",n)
else:
    print("Fibonacci series")
    while count < n:
        print(a)
        n=a+b
        a=b
        b=n
        count += 1"""


x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y


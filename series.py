

'''num=int(input("enter a number"))
sum=0
avg=0.0
for i in range(1,num+1):
    sum = sum+i
avg = sum/i
print("sum")
print("avg")'''

'''#multiplication table
num=int(input("enter a number"))
for i in range(1,11):
   print(num, "X", i , "=" , num*i)'''



"""#leap year
for i in range(1900,2020):
   if i%4==0:
      print(i, end=" ")"""

'''n=int(input("enter the nth term" ))
s=0
for i in range(1,n+1):
    a=1/i
    s=s+a
print("the sum of 1,1/2...1/"+str(n)+"is"+str(s))'''


"""n=int(input("enter the nth term" ))
sum=0
for i in range(1,n+1):
    a=1/(i**2)
    sum=sum+a
print("the sum of 1,1/2...1/"+str(n)+"is"+str(sum))"""


'''num1=int(input("enter a value"))
num2=int(input("enter b value"))
sum=num1-num2
print(sum)'''



'''#problem statement to find a number in given list of series
#series 0,0,7,6,14,12,21,18.....
n=int(input("enter the position"))
a=b=0
for i in range(1,n+1):
    if(i%2!=0):
        a=a+7
    else:
        b=b+6
if n%2!=0:
    print('{} at accordance {}'.format(n,a-7))
else:
    print('{} at accordance {}'.format(n, b-6))'''


'''#another method
n=int(input())
list=[]
for i in range(0,n+1):
    a=7*i
    list.append(a)
    b=6*i
    list.append(b)
print(list)
l=len(list)
num=int(input("enter position:"))
for i in range(l):
    if i==num-1:
       print(num)'''



'''#number series type 2
#series 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187...
n=int(input("enter the position:"))
a=b=1
for i in range(0,n-1):
    if(i%2!=1):
        a=a*2
    else:
        b=b*3
if n%2!=0:
    print('{} at accordance {}'.format(n,a))
else:
    print('{} at accordance {}'.format(n,b))'''


'''n=int(input("enter the position"))
a=b=0
for i in range(1,n+1):
    if(i%2!=0):
        a=(a*i)+7
    else:
        b=(b*i)+6
if n%2!=0:
    print('{} at accordance {}'.format(n,a))
else:
    print('{} at accordance {}'.format(n,b))'''



str1 = "ABCDEFGH"
str2 = "ate"
for letter in str1:
    print(letter + str2, end = " ")
    print('\n')



 
 

   

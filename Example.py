"""a = "hello"
print(a.upper())"""

"""
i=0
while(i<=10):
        print(i,end = '\t')
        i+=1
"""

"""i=3  #static
sum=0
while(i<=9):
    sum=i+sum
    print(sum)
    i+=1"""


"""#dynamic
m = int(input())
n = int(input())
sum = 0
while(m<=n):
    sum= sum + m
    m = m+1
    print("sum=", sum)"""




"""sum=0
n=int(input("enter a 3 digit number"))
while(n!=0):
   temp = n%10
   sum = sum + temp
   n = n// 10
   print("the sum of digit", sum)"""


"""#program to check nivens
n=int(input("enter a 3 digit number"))
sum=0
rem=0
temp= n
while(temp>0):
    rem = temp%10
    sum = sum + rem
    temp = temp//10
print("sum = ", sum)
if (n%sum == 0):
    print("nivens number")
else:
     print("Not nivens number")"""



"""#reverse of number"
n=1234
n_string = str(n)
r_num = "".join(reversed(n_string))
print("reversed number is:" + r_num)


def reverse(n):
    if len(n)==0:
        return n
    return reverse(n[1:]) +n[0]
num = 1234
n_string = str(num)
r_num = reverse(n_string)
print("reverse number is:" +r_num)"""


"""
n= int(input())
rev = 0
while(n>0):
   rem=n%10
   rev=(rev*10)+rem
   n = n//10
print(rev)"""

'''n= int(input())
while(n>0):
   temp=n%10
   print(temp, end=" ")
   n = n//10'''


n= int(input())
m= input().split(" ")[:int(n)]
rev = 1
for i in range(n):
   rev=rev*int(i)
print(rev)
rev=1

   

#function - space is allocated in the memory location

#function is into 2 parts

"""1. function header
2. function body

syntax: def fun_name(var1,var2....):
    documentation string
    statement block
    return[expression/value]
no arguments- noreturn values
example:
    def fun():------callee
        for i in range(10)
        print("abcde")
    fun()-------caller
arguments passed worj return values"""
#example:
"""def add(x,y):
   return x+y
a=10
b=20
operation=add
print(operation(a,b))



def fun():
    for i in range(10):
        print("abcder")
fun()

def num():
    for i in range(10):
        print(i)
num()"""


def add(x,y):
   z=x+y
   print(z)
def sub(x,y):
   z=x-y
   print(z)
def Mul(x,y):
   z=x*y
   print(z)
x=int(input())
y=int(input())
add(x,y)
sub(x,y)
Mul(x,y)

#global variable
"""v="hi"
def abc():
    global v2
    v2 ="goodmorning"
    print(v)
abc()
print(v)
print(v2)"""

"""#modify global variable
v1="hi"
def abc():
    global v1
    v1 ="goodmorning"
    print("in the function v1 is-",v1)
abc()
print("outside function is v2",v1)
v1="verygood"
print("outside function after modify",v1)"""


"""#program to demo access of var in inner & outer function

def outer_fun():
    outer_var=11
    def inner_fun():
        inner_var=12
        print("inner variable",inner_var)
    inner_fun()
    print("outer variable",outer_var)
outer_fun()"""



#writing a function and return its cubation format

"""def cube(x):
    return(x*x*x)
num=10
result = cube(num)
print(result)"""


"""def cube(x):
    return(x*x*x)
num=10
print(cube(num))"""

#writing a function to understand a mismatch parametres

"""def fun(i):
    print("orange",i)
j=10
fun(j)"""

"""
def fun(i):
    print("orange",i)
fun(5+5*3)

def fun(i):
    print("orange",i)
fun(10)
"""

#program to demo key args

"""def display(str,int_x,float_y):
    print("the string is",str)
    print("the integer is",int_x)
    print("the float is",float_y)
display(float_y=34.66,str="manasa",int_x=234)"""


"""def display(str,int,float):
    print("the string is",str)
    print("the integer is",int)
    print("the float is",float)
display(float=34.66,str="manasa",int=234)"""
"""
def display(name,age,salary):
    print("Name is",name)
    print("age is",age)
    print("salary ",salary)
x="Manasa"
y=19
z=123456
display(name=x,age=y,salary=z)"""


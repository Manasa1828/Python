#Abstract class
#its the process of handling the information by hiding the informal unnecessary information to the user
#meta class access the instance from another class
"""
class fruit:
    def taste(self):
        raise NotImplementedError()
    def rich(self):
        raise NotImplementedEroor()
    def color(self):
        raise NotImplementedError()
class Mango(fruit):
    def taste(self):
        return "sweet"
    def rich(self):
        return "vitamin A"
    def color(self):
        return " Golden Yellow"
class Orange(fruit):
    def taste(self):
        return "sour"
    def rich(self):
        return "vitamin C"
    def color(self):
        return "Orange"
Alphanso = Mango()
print(Alphanso.taste(), Alphanso.rich(), Alphanso.color())
Orange = Orange()
print(Orange.taste(), Orange.rich(), Orange.color())
"""


"""#program to interviene ploymorphism on a complex number

class complex():
    def __init__(self):
        self.real = 0
        self.img = 0
    def setValue(self,real,img):
        self.real = real
        self.img = img
    def __add__(self,c):
        temp = complex()
        temp.real = self.real+c.real
        temp.img = self.img+c.img
        return temp
    def disp(self):
        print("(",self.real, "+", self.img, "i)")
c1=complex()
c1.setValue(2,3)
c2=complex()
c2.setValue(4,5)
c3=c1+c2
print("result is...")
c3.disp()"""


#operator ----- function name-----
# +     __add__
# +=    __iadd__
# -     __sub__
# -=    __isub__
# *     __mul__
# *=    __imul__
# /     __truediv__
# /=    __idiv__
# **    __pow__
# **=   __ipow__
# %     __mod__
# %=    __imod__
# >>    __rshift__
# >>=   __irshift__
# &     __and__
# &=    __iand__
# |     __or__
# |=    __ior__
# ^     __xor__
# ^=    __ixor__
# ~     __invert__
# ~=    __iinvert__
# >     __gt__
# <     __lt__
# >=    __ge__
# <=    __le__



# program that has abstract class to derive 2 classes
# rectangle and traingle from polygon class and write the methods to get their details and dimensions and hence calculate the area respectively
"""
class polygon:
    def get_data(self):
        raise notImplementedError()
    def area(self):
        raise notImplementedError()
class rectangle(polygon): 
    def get_data(self):
        self.length = float(input("enter rectangle len"))
        self.breadth = float(input("enter reactangle breadth"))
    def area(self):
        return self.length * self.breadth
class triangle(polygon):
    def get_data(self):
        self.base = float(input("enter triangle base"))
        self.height = float(input("enter triangle height"))
    def area(self):
        return 0.5 * self.base * self.height
R = rectangle()
R.get_data()
print("area of a rectangle", R.area())
T = triangle()
T.get_data()
print("area of a triangle", T.area())
"""


"""
#encapsualing  public members

class pub:
    def __init__(self,name,num):
        self.name = name
        self.num = num
    def Num(self):
        print("roll num is", self.num)
obj = pub("harry", 299)
obj.Num()
"""

#program to over-ride get-item and set-item methods
"""
class mylist:
    def __init__(self,list):
        self.list = list
    def __getitem__(self,index):
        return self.list[index]
    def __setitem__(self,index,num):
        self.list[index]=num
    def __len__(self):
        return len(self.list)
    def disp(self):
        print(self.list)
l = mylist([1,2,3,4,5,6,7,8,9])
print("list is .........")
l.disp()
index = int(input("enter the index of the list "))
print(l[index])
num = int(input("enter the position u want to modify"))
l[index] = num
l.disp()
print("the length of list is", len(l))
"""
#special or miscellaneous functions in overloading
class number:
    def __init__(self,num):
        self.num = num
    def disp(self):
        return self.num
    def __abs__(self):
        return abs(self.num)
    def __float__(self):
        return float(self.num)
    def __hex__(self):
        return hex(self,num)
    def __oct__(self):
        return oct(self.num)
    def __setitem__(self,num):
        self.num=num
n = number(-14)
print("n is = ", n.disp())
print("abs(n) is = ", abs(n))
n = abs(n)
print("converting to float", float(n))
print("converting to hexa", hex(n))
print("converting to octa", oct(n))

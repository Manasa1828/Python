##program to access a class variable using a class object


"""class Ex:
    var=22
obj = Ex()
print(Ex.var)"""


#program to access a class member using a class object
"""class abc:
    var=12
    def display(self):
        print("this is class method")
obj = abc()
print(obj.var)
obj.display()"""


"""class abc:
    var=12
    var2=18
obj = abc()
print(obj.var)
print(obj.var2)"""


#program to illustrate the constructor// method always should be written in function only
#_init_().... method double(__)
"""class abc:
    def __init__(self,var1):
        print("in class method")
        self.var1=var1
        print("the value",var1)
obj=abc(20)

class abc:
    def __init__(self,val,val2):
        print("in class method")
        self.val=val
        self.val2=val2
        print("the value",val)
        print("the value",val2)
obj=abc(20,30)"""



#program to differentiate

"""class abc():
    class_var = 0
    def __init__(self,var):
        abc.class_var+=1
        self.var = var
        print("the obj var ", var)
        print("the class value of c-=var",abc.class_var)
obj1=abc(20)
obj2=abc(30)
obj3=abc(40)"""

#program illustrating a modification on numberics
"""class Number:
    even=0  #default value
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num," is even")
        else:
            print(num,"is odd")
obj=Number()
obj.even_odd(21)"""


"""
class Number:
    evens=[]
    odds=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)
n1=Number(1)
n2=Number(3)
n3=Number(4)
n4=Number(7)
n5=Number(6)
n6=Number(12)
print("even numbers", Number.evens)
print("odd numbers", Number.odds)"""

#delete  method--- c++/java analogus to destructors
#general syntax __del__
"""
class abc():
    class_var=0
    def __inti__(self, var):
        abc.class_var+=1
        self.var = var
        print("the obj var ", var)
        print("the class value of c-=var",abc.class_var)
    def __del__(self):
        abc.class_var -=1
        print("object with value %d is going out of scope ",self.var)
obj1=abc(20)
obj2=abc(30)
obj3=abc(40)
del obj1
del obj2
del obj3
"""

"""class abc():
    class_var = 0
    def __init__(self,var):
        abc.class_var+=1
        self.var = var
        print("the obj var ", var)
        print("the class value of c-=var",abc.class_var)
obj1=abc(20)
obj2=abc(30)
obj3=abc(40)"""



#__repr__ -----syntax report of the object
#__cmp__ -------- compare two class objects
# __len__ -----len(object)
#__call__ ------ it acts like a func to call its instances
# __lt__, __le__,__eq__, __ne__, __gt__, __ge__, --- to compare 2 objects
# __iter__ iteration over an object
# __getitem__used for indexing  gs:def __getitem(self,var/key)
#set item assign an item to the indexed value


#program to demonstate get and set items in a list
"""
class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self, index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
print(numlist[3])
print(numlist.mylist)
numlist[3]=10
print(numlist.mylist)
print(numlist[3])
print(numlist.mylist)
numlist[3]=5"""
    


"""
class xyz():
    class_var=0
    def __inti__(self, var):
        xyz.class_var+=1
        self.var = var
        print("the obj var ", var)
        print("the class value of c-=var",xyz.class_var)
    def __del__(self):
       xyz.class_var-=1
       print("object with value %d is going out of scope ",self.var)
obj1=xyz(20)
obj2=xyz(30)
obj3=xyz(40)
del xyz1
del xyz2
del xyz3"""


"""
class ABC():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var - obj.var
obj = ABC("abcdef",10)
print("the value sorted in obj is", repr(obj))
print("the lenght of the name sorted in obj", len(obj))
obj1 = ABC("ghijkl",1)
val = obj.__cmp__(obj1)
if val==0:
    print("both values are equal")
elif val==-1:
    print("1st values is less than second")
else:
    print("2nd values is less than 1st")
"""


"""
#is for illustrating use of a private method
class abc():
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("this from class method,var = ", self.__var)
obj = abc(10)
obj._abc__display()"""


#to call a class method form another method of same class
"""class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is = ", self.var)
    def add_2(self):
        self.var +=2
        self.display()
obj = abc(10)
obj.add_2()"""



#program to show how a class method calls a function
#which is defined in the global name space
"""
def scale_10(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is=",self.var)
    def modify(self):
        self.var = scale_10(self.var)
obj = abc(10)
obj.display()
obj.modify()
obj.display()
"""

#built-in attributes
#for get set and delete
# .. hasattr(obj,name)-checks obj possesses the attributes values or not

#..getattr(obj,name[,default])
# setattr(obj,name,value)-- which is used to set an attribute of the object
# detattr(obj,name)

"""
#program to demo builtin
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is", self.var)
obj = abc(10)
obj.display()
print("check whether obj has attribute var?", hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',50)
print("after setting value,var is", obj.var)
setattr(obj,'count', 10)
print("new variable count is created  and its val=", obj.count)
delattr(obj, 'var')
setattr(obj,'var', 40)
print("after deleting the attr, var is:",obj.var)"""

"""
#built-in class attributes
1. .__dict__
2. .__doc__ class documentation string when it is specified it will access a class other wise it will return null value
3. .__name__ it will define  name of module in which class is define
4. .__bases__ to return the bases class"""


"""class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("var1 is =",self.var1)
        print("var2 is =",self.var2)
obj = abc(10,12.34)
obj.display()
print("object.__dict__-", obj.__dict__)
print("object.__doc__-", obj.__doc__)
print("object.__name__-", abc.__name__)
print("object.__module__-", obj.__module__)
print("object.__bases__-", abc.__bases__)"""


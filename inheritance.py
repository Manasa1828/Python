#to visualize inheritance flow
"""
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print("name is", self.name)
        print("age is", self.age)
class teacher(person):
    def __init__(self,name,age,exp,rarea):
        person.__init__(self,name,age)
        self.exp=exp
        self.rarea=rarea
    def dispdate(self):
        person.disp(self)
        print("experience is", self.exp)
        print("research area", self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
        person.disp(self)
        print("course=",self.course)
        print("marks=",self.marks)
print("------------teacherclass-------")
T= teacher("Mark", 74,53,"jss")
T.dispdate()
print("---------------student---------")
s= student("Manasa",19,"B.tech",778)
s.disp()
"""

#program to invoke __init__in multiple inheritance
"""
class base1(object):
    def __init__(self):
        print("base class 1")
class base2(object):
    def __init__(self):
        print("base class 1")
class Derived(base1,base2):
    pass
D= Derived()
"""


#program to call constructor of a base class from super
"""class base1(object):
    def __init__(self):
        print("base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    pass
D= Derived()
"""

"""
class base1(object):
    def __init__(self):
        print("base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    def __init__(self):
        super(Derived,self).__init__()
        print("Derived class")
D= Derived()
"""
"""
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print("name is", self.name)
        print("age is", self.age)
class teacher(person):
    def __init__(self,name,age,exp,rarea):
        person.__init__(self,name,age)
        self.exp=exp
        self.rarea=rarea
    def dispdate(self):
        person.disp(self)
        print("experience is", self.exp)
        print("research area", self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
        person.disp(self)
        print("course=",self.course)
        print("marks=",self.marks)
print("------------teacherclass-------")
T= teacher("Mark", 74,53,"jss")
T.dispdate()
print("---------------student---------")
s= student("Manasa",19,"B.tech",778)
s.disp()
print("T is a teacher:", isinstance(T,teacher))
print("T is a integer:", isinstance(T,integer))
print("T is a person:", isinstance(T,person))
print("T is a object:", isinstance(T,object))
print("person is a subclass of teacher", issubclass(person,teacher))
print("teacher is a subclass of person", issubclass(teacher,person))
"""
"""
class person:
    def name(self):
        print("name is ...")
class teacher(person):
    def qual(self):
        print("qualification is phd")
class hod(teacher):
    def expe(self):
        print("experiance is 22 years")
HOD= hod()
HOD.name()
HOD.qual()
HOD.expe()
"""

#multi path inheritance
class student:
    def name(self):
        print("name....")
class academic(student):
    def acad_score(self):
        print("academic score 90% above")
class CSE(student):
    def CSE_score(self):
        print("CSE SCORE ------60% AND ABOVE")
class result(academic,CSE):
    def eligibility(self):
        print("--------eligibility to apply-------")
        self.acad_score()
        self.CSE_score()
R= result()
R.eligibility()

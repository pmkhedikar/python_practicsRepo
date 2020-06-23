## Class
# class phone():
#
#     def __init__(self, ram, memory):
#         self.ram = ram
#         self.memory = memory
#
#     def config(self, ram, memory):
#         print( 'config is :', self.ram, self.memory )
#
#
# phone1 = phone('2','32gb')
# phone1.config('2','32gb')


## self & Constructor
## Self represents the instance of the class. By using the “self” keyword we can access the attributes(Variable) and methods(fuction) of the class in python.
## "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology.
## This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
#
# class Phone:
#
#     def __init__(self):
#         self.name = 'Moto'
#         self.price = 10
#
#     def update(self):     #update name inside the class
#         self.name ='new Phone'
#         self.price = 20
#
#     def compare(self,other):
#         if self.price == other.price:
#             return True
#         else:
#             return False
#
#
# p1 = Phone()
# p2 = Phone()
# # p1.name ='iphone'     #update name 1 outside the class
# # print(p1.name)
# #
# # p2.update()         #called update method to change the name
# # print(p2.name)
#
# # p2.update()
# # p2.price =30
# print(p1.price)
# print(p2.price)
# print(p1.compare(p2))

# # Type of Variable - Instance/Static Variable & Class variable

# class Car():
#
#     wheels = 4                #class/static variable
#
#     def __init__(self):
#         self.name = 'VOLVO'   # Instance Variable
#         self.color = 'RED'
# c1 = Car()
# c2 = Car()
# c2.name = 'BMW'  # update the name of an object c2
# Car.wheels = 6   # update the class variable Variables
#
# print(c1.name,c1.color,c1.wheels)
# print(c2.name,c2.color,c2.wheels)


## Instance Method , Class method ,Static Method
#
# class School():
#
#     schoolName = 'NPK SCHOOL'
#
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     @classmethod                    # class Method
#     def GetSchoolName(cls):
#         return cls.schoolName
#
#     @staticmethod
#     def principle():                          # Static Method
#         print('This is static method not passing any self keyword')
#
#
#
# s1 = School(10,20,30)
# print(s1.avg())  # calling instance method
# print(School.GetSchoolName())  # calling class method
# School.schoolName = 'MIET'     # Updated the class/static variable
# print(School.GetSchoolName())  # calling class method
# School.principle()             # calling static method not passed an argument


## Inner Class in Python
## Can create the object of child class in parent class
# ## Can create the object of child class outside the parent class - but u have to call the parent class
#
# class Student():
#
#     def __init__(self,name,rollNo):
#         self.name = name
#         self.rollNo = rollNo
#         self.lap = self.laptop()
#
#     def show(self):
#         print(self.name,self.rollNo)
#         self.lap.show()
#
#     class laptop():
#         def __init__(self):
#             self.brand = 'Mac'
#             self.ram = '4gb'
#             self.cpu = 'ios5'
#
#         def show(self):
#             print(self.brand,self.ram,self.cpu)
#
# s1 = Student('Parag',684)
# s2 = Student('Arvind',101)
# print(s1.name,s1.rollNo,s2.name,s2.rollNo)
# lap1 = s1.laptop()
# print(lap1.brand)
# s1.show()
# print(lap1.brand,lap1.ram)
# lap1 = Student.laptop()
# print(lap1.brand,lap1.ram,lap1.cpu)


############################################################################# Inheritance Parent - child relation
##  Inheritance allows us to define a class that inherits all the methods and properties from another class
# class A:
#     def feature1(self):
#         print('Class A - Feature 1')
#     def feature2(self):
#         print('Class A - Feature 2')
#
# class B(A):
#     def feature3(self):
#         print('Class B - Feature  3')
#     def feature4(self):
#         print('Class B - Feature 4')
#
# class C(A,B):
#     def feature5(self):
#         print( 'Class C - Feature  5' )
#
# a1 = A()        # As its parent class ,uses the method of class A only
# a1.feature1()

# b1 = B()         #Can access all the methonds in A & B class
# b1.feature2()
#
# c1 = C()
# c1.feature4()   # Multilevel Inheretance can access method in both A & B class



################################################################# - Constructor in inheritance
## 1. if __init__ method not found in sub-class exexute the __init__ in parent class
## 2. if __init__ method found in sub-class execute the __init__ in subclass
## 3. if want to call __inti__ in parent class use the keyword super to call the method in parent class
## MRO - method resolution order  - Give the preference from left to right C(B,A)

# class A:
#     def __init__(self):
#         print('Class -A ,init method')
#     def feature1(self):
#         print('Class A - Feature 1')
#     def feature2(self):
#         print('Class A - Feature 2')
#
# class B:
#     def __init__(self):
#         #super().__init__()
#         print('Class -B ,init method')
#     def feature3(self):
#         print('Class B - Feature  3')
#     def feature4(self):
#         print('Class B - Feature 4')
#
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         print('Class -C ,init method')
#     def feature5(self):
#         print( 'Class C - Feature  5' )
#
# c1 = C()



################################################################################# Polymorphism (Many + Form)
## concept of using common operation in diff ways for diff data inputs
## 1.Duck typing - Interface / class should have that method that what we concern
## you shouldn't care what type of object you have - just whether or not you can do the required action with your object.
# class Pycharm:
#     def execute(self):
#         print('Compliling')
#         print('Error Checking')
#
# class Myeditor:
#     def execute(self):
#         print('Spell checking')
#         print('Syntax checking')
#         print('Compliling')
#         print('Error Checking')
#
#
# class Laptop:
#     def code(self,ide):
#         ide.execute()
#
# ide1 = Pycharm()
# ide2 =Myeditor()
# lap1 = Laptop()
# lap1.code(ide2)


### Operator Overloading - Every operator has its own behaviour and that define behind the screen, if we want to change the behaviour of that operator depends upon our need thats called operator overloading
### Same method with different argument eg. __add__()
## We can overload all existing operators but we can't create a new operator

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         a1 = self.m1 + other.m1
#         a2 = self.m2 + other.m2
#         add = a1 + a2
#         return add
#
#     def __str__(self):
#         #return self.m1,self.m2   -return a tuple
#         return '{} {}'.format(self.m1,self.m2)  #converted into string
#
# s1 = Student(10,20)
# s2 = Student(100,200)
# print(s1.m1,s1.m2)
# s3 = s1 + s2
# print(s3)
#
# a = 5
# print(a)
# print(s1.__str__())  # uncomment - return self.m1,self.m2   -return a tuple
# print(s1)


### Method Overloading
### A class having same method with different parameter/argument called method overloading

# class  Student():
#     def __init__(self):
#         self.m1 = 10
#         self.m2 = 20
#
#     def sum(self,a=None,b=None,c=None):
#         if a != None and b != None and c != None:
#             return a+b+c
#         elif a != None and b !=None:
#             return a+b
#         else:
#             return a
# s1 = Student()
# print(s1.sum(1,2))


### Method Overridding
## Override means having two methods with the same name but doing different tasks.
## It occurs by simply defining in the child class a method with the same name of a method in the parent class

# class A:
#     def show(self):
#         print('Show Method in Class A')
#
# class B(A):
#     def show(self):
#         print('Show Method in Class B')
#
#     pass
#
# a = B()      #Created a object for class B
# a.show()     # It will first search the method in class B & if not found then check in class A
#

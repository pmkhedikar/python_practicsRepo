# ## Example 1: Creating Class and Object in Python
# class Man:
#     gender = 'Male'  # class attributes
#     spcies = 'Human'
#
#     def __init__(self, name, age):  # Instance attribute
#         self.name = name             #__init__ is initializing method its run first asa object created
#         self.age = age
#
#
# parag = Man('Parag', 23)  # instantiate the Man class
# rahul = Man('Rahul', 34)
#
# print(parag.name, parag.age)
# print(parag.__class__.gender)
# print(parag.__class__.spcies)
# print(parag.__class__.spcies)


##Example 2 : Creating Methods in Python
# Methods are fn defined inside the class & they used to define the behaviour of an object

class Man:
    gender = 'Male'
    species = 'Human'

    # Instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # Instance method cause called on instance object
    def read(self, book):
        return self.name, book

    def dance(self):
        return self.name


parag = Man('Parag', 32)

print(parag.read('Automic Habit'))
print(parag.dance())



###
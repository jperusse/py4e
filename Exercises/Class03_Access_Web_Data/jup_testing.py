# %%
import json
print("Hello world")
# %%

# %%


class Computer:
    __maxprice = 900

    def __init__(self):
        #    self.__maxprice = 900
        pass

    def sell(self):
        print('Selling Price: {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(2000)
c.sell()
# %%
class Bird:

   def __init__(self):
     print('Bird is ready')

   def whoisThis(self):
     print('Bird')

   def swim(self):
     print('Swim faster')

# child class
class Penguin(Bird):

   def __init__(self):
     # call super() function
     super().__init__()
     print('Penguin is ready')

   def whoisThis(self):
     print('Penguin')

   def run(self):
     print('Run faster')

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
# %%
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
    def tell(self):
        '''Tell my details.'''
        print('Name:{} Age:{}'.format(self.name, self.age), end=' ')
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {:d}'.format(self.marks))
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# prints a blank line
print()
members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
# %%
class Parrot:

 def fly(self):
   print('Parrot can fly')

 def swim(self):
   print('Parrot can not swim')

class Penguin:

 def fly(self):
   print('Penguin can not fly')

 def swim(self):
   print('Penguin can swim')

# common interface
def flying_test(bird):
  bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
# %%
class Parrot:

# class attribute
 species = 'bird'

# instance attribute
 def __init__(self, name, age):
    self.name = name
    self.age = age
    self.species = 'fred'

# instantiate the Parrot class
blu = Parrot('Blu', 10)
woo = Parrot('Woo', 15)

# access the class attributes
print('Blu is a {}'.format(blu.__class__.species))
print('Woo is also a {}'.format(woo.__class__.species))
# access the instance attributes
print('{} is {} years old'.format( blu.name, blu.age))
print('{} is {} years old'.format( woo.name, woo.age))
print('{} is a {}'.format( woo.name, woo.species))
# %%
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)
p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
# %%
class Parrot:

# instance attributes
 def __init__(self, name, age):
   self.name = name
   self.age = age

# instance method
 def sing(self, song):
   return '{} sings {}'.format(self.name, song)

 def dance(self):
   return '{} is now dancing'.format(self.name)

# instantiate the object
blu = Parrot('Blu', 10)
# call our instance methods
print(blu.sing('Happy'))
print(blu.dance())
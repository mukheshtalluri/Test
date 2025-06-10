# Single inheritance : Child will inherit properties from the single parent.
class Animal:
    def speak(self):
        print('Animal will speak')

class Dog(Animal): # While inheriting child class can access to the parent class methods.
    def bark(self):
        print('Dog bark')

d = Dog()
d.speak()
d.bark()

# Multiple inheritance : Child can inherit properties from the multiple parents.
class Father:
    def skills(self):
        print('Coding, Gardening')

class Mother:
    def hobbies(self):
        print('Cooking, Painting')

class Child(Father, Mother):
    def talents(self):
        print('Signing')

c = Child()
c.skills()
c.hobbies()
c.talents()

# Multilevel Inheritance : Child can inherit properties from the parent as well as grandparent.
class Grandparent:
    def house(self):
        print('Grandparent\'s home.')

class Parent(Grandparent):
    def car(self):
        print('Parent\'s car')

class Child(Parent):
    def bike(self):
        print('Child\'s bike.')

c = Child()
c.house()
c.car()
c.bike()

# Hierarchical inheritance : Multiple child inherit properties from the same parent.
class Parent:
    def profession(self):
        print('Software Engineer')

class Son(Parent):
    def education(self):
        print('Chemical Engineering')

class Daughter(Parent):
    def education(self):
        print('Aerospace Engineering')

s = Son()
s.profession()
s.education()

d = Daughter()
d.profession()
d.education()

# Hybrid inheritance : Inheritance will be happened multiple types like multilevel, hierarchical inheritance.
class A:
    def method_a(self):
        print('From A')

class B(A):
    def method_b(self):
        print('From B')

class C(A):
    def method_c(self):
        print('From C')

class D(B, C):
    def method_d(self):
        print('From D')

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()

# Access the parent attributes from the child class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        return f'My self {self.name} and I am {self.age} old.'

class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

emp = Employee('Mukhesh', 27, 'Software Engineer')
print(emp.person_info())

# One more use case
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child:
    def __init__(self, parent: Parent, grade):
        self.parent = parent
        self.grade = grade

    def show_info(self):
        print(f"Name: {self.parent.name}")
        print(f"Age: {self.parent.age}")
        print(f"Grade: {self.grade}")


p = Parent("Alice", 40)
c = Child(p, "10th Grade")
c.show_info()

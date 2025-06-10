# Classes : Class is the blueprint to define an object. Class will define the methods and variables for the object.
# Object : Object is the real world entity which is derived from the class.

# Class : Person is class where we define attribute and methods.
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello {self.name}.'

# object : person is object which we can create using class. object has access to the all attributes and methods.
person = Person('Mukhesh')
print(person.greet())
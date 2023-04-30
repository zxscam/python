from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age
    @abstractmethod
    def say(self):
        print('wepp')

class Cat(Animal):
    def say(self):
        print('Meow!')

class Dog(Animal):
    def say(self):
        print('Woof!')
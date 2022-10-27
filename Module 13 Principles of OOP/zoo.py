
from abc import ABC, abstractmethod

# abstract base method

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def move(self):
        print('hanging on the branches of the trees')

class Monkey(Animal):
    def sing(self):
        print('monkey is signing')
    def eat(self):
        print('eating banana')
    def name(self):
        pass
    def move(self):
        print('hanging on the branches of the trees')

layka = Monkey()
# print(layka)
layka.eat()
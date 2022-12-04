#abstract class/ method
from abc import ABC, abstractmethod

class Vehicle(ABC): #blue print of a class
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print('I am a car')
    def stop(self):
        print('Stop your car')
class Motor(Vehicle):
    def go(self):
        print('I am a Motor')
    def stop(self):
        print('Stop your Motor')

Car = Car()
Car.go()
Car.stop()

Motor = Motor()
Motor.go()
Motor.stop() 

''' Abstraction is the concept of  the complex details
 and showing the necessary features of an object. 
This helps in reducing programming complexity and efforts.'''
'''ABC makes sure ki jo fxn @abstract method keniche hai 
wo hr wo class me rehna chahiye jo ABClass ke bad bn rha ho
aur agr aisa nhi huwa toh it will throw error. Aur isse ye
ye fayda hota hai ki hr ek class ko wo particular fxn 
ko apne hisab se return kr skta hai'''

from abc import ABC,abstractmethod
# Abstract Base Class
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("car engine started.")
def operate_vehicle(vehicle):
  vehicle.start_engine()
car=Car()
operate_vehicle(car)
'''rather than makinf a fxn like operate_engine 
we can directly call it using subclass name'''
car.start_engine()
'''------------------- Krish Naik Sir ------------------------------------'''
''' ------------------ example from gfg ----------------------------------'''
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")
c=Dog()
c.move()



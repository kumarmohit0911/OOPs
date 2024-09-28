''' Abstraction is the concept of  the complex details
 and showing the necessary features of an object. 
This helps in reducing programming complexity and efforts.'''
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
"------------------- Krish Naik Sir ------------------------------------"


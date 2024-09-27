'''Problem:- Create two class battery & engine & 
let the ElectricCar class inherit from both,
demostrating multiple inheritance.'''
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
    def get_brand(self):
        return self.__brand + "!"
    def fuel_type(self):
        return "petrol or diesel"
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size 
    def fuel_type(self):
        return "Electric charge"
class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "this is engine"
class ElectricCarTwo(Battery,Engine,Car):
    pass
my_new_tesla=ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.engine_info())


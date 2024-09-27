'''Problem:- Create two class battery & engine & 
let the ElectricCar class inherit from both,
demostrating multiple inheritance.'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
    def get_brand(self):
        return self.__brand + "!"
    def fuel_type(self):
        return "petrol or diesel"

class Battery:
    def __init__(self,watt):
        self.watt=watt
    def battery_info(self):
        return f"this car has battery of {self.watt} ."
class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power
    def engine_info(self):
        return f"this car has {self.horse_power} engine"

        
class ElectricCarTwo(Battery,Engine,Car):
    def __init__(self, brand, model,watt,horse_power):
        Car.__init__(self,brand,model)
        Engine.__init__(self,horse_power)
        Battery.__init__(self,watt)

my_new_tesla=ElectricCarTwo("Tesla","Model S","160kwh","100 HP")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())


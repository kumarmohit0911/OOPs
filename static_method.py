'''Problem:- Add a static method to Car class 
that returns a general description of a car.'''
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.total_car+=1 
    def full_name(self):
        return f"{self.brand} {self.model}"
    def get_brand(self):
        return self.__brand + "!"
    def fuel_type(self):
        return "petrol or diesel"
    @staticmethod
    def general_description():
        return "Cars are mean of transport"
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size 
    def fuel_type(self):
        return "Electric charge"
my_tesla=ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.fuel_type())
safari=Car("tata","safari")
safariThree=Car("tata","nexon")
print(safari.fuel_type())
print(Car.total_car)
print(Car.general_description())
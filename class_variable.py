'''Problem:- Add a class variable to Car that keeps
track of the numbers of cars created.
Solution:- count how many times __init__ method
has been called. qki jitni bar car add hongi
utni bar __init__ call hogi'''
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.total_car+=1 #shows how many times __init__ method has been initiated
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
my_tesla=ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.fuel_type())
safari=Car("tata","safari")
safariThree=Car("tata","nexon")
print(safari.fuel_type())
print(Car.total_car)# as total_car is class variable
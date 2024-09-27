'''Problem:- use a property decorator in the Car
class to make the 'model' attribute read-only.
-------------------------------------------------
elaboration:-
jo ek model hota hai wo change ho skta hai agr 
user usko change krna chahe toh. for example ek 
car aur uska model diya huwa hai aur koi bahar ka aake
usko change kr deta hai. maan lo ki koi user ake
kisi bank acc ka surname hi change kr diya. so to stop that 
kind of issues we use property decorators taki access 
private na krke read only kr de.. taki user dekh toh paye or change na kr paye'''

class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1 
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def get_brand(self):
        return self.__brand + "!"
    def fuel_type(self):
        return "petrol or diesel"
    @staticmethod
    def general_description():
        return "Cars are mean of transport"
    @property # by this decorator we can make model attribute unchangeable
    #which will not let the my_car.model="city" change the already existing model.
    def model(self):
        return self.__model
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size 
    def fuel_type(self):
        return "Electric charge"
my_car=Car("tata","safari")

#print(Car.general_description())
#my_car.model="City"# by this we can change the model
print(my_car.model)

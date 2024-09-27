class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
my_car=Car("Maruti", "Alto")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
my_new_car=Car("Tata","Safari")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())
print(f"----------inheritence will start from  here--------")
# battery class inheriting from Car class
class ElectricCar(Car):# by adding Car here we are inheriting everything
    def __init__(self,brand,model,battery_size):
        '''self.brand=brand we can write this..
        but why? we have already written all that earlier 
        and aisa thodi hai 15 bar bna rhe to 15 bar likhenge same chiz
        isliye thoda sa kam upr wale se hi chla lete hain'''
        super().__init__(brand,model)
        self.battery_size=battery_size #as this functionality doesn't exixt above
my_tesla=ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.model)
print(my_tesla.full_name())
print(f'----------------inherience ends here--------------')
#-------inheritence ends here--------

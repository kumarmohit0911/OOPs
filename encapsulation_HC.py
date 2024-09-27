#-------- encapsulations starts here---------
# Problem: Modify the Car class to 
# encapsulate the brand attribute, 
# making it private, and provide a getter method for it
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
    def get_brand(self):
        return self.__brand + "!"
class ElectricCar(Car):# by adding Car here we are inheriting everything
    def __init__(self,brand,model,battery_size):
        '''self.brand=brand we can write this..
        but why? we have already written all that earlier 
        and aisa thodi hai 15 bar bna rhe to 15 bar likhenge same chiz
        isliye thoda sa kam upr wale se hi chla lete hain'''
        super().__init__(brand,model)
        self.battery_size=battery_size #as this functionality doesn't exixt above
my_tesla=ElectricCar("Tesla","Model S","85kWh")
#print(my_tesla.__brand()) won't work
#as double underscore will make it private.

print(my_tesla.get_brand())
'''encapsulation mtlb bahari world se chizo ko encapsulate
 kr diya( yani chhipa diya ya private kr diya)'''
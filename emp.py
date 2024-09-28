class Employee:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i
# As there is no __str__ it gives some value like 
#<emp.Employee object at 0x000002971BAC0560> on printing.
    def __str__(self):
        return f"The name of the employee is {self.name} and lenght of the name is {len(self)}"
    #To return the length of the employee's name in the __str__ method, you can simply use the len(self) function, which will internally call the __len__ method that you've defined.
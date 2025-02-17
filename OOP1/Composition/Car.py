# Car.py
from Engine import Engine  # Importing the Engine class from Engine.py       

class Car:
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)  # Composition: Engine is part of Car

    def start(self):
        print(f"{self.make} {self.model} is starting.")
<<<<<<< HEAD
        self.engine.start1()


class radio:
    def  __init__(self, status):
        self.status = status    #  On/Off
        
    @property
    def status(seft): 
        return " สถานะวิทยุ : "+self.status   
    
    @status.setter
    def status(self): 
        if self.status=="On" :
            self.status="Off"   
        else:
            self.status=="On"     
    
    def show(self):
        print(f" สถานะวิทยุ : {self.status}") 
        

car = Car("Toyota", "Camry", 200)
car.start()


'''

class radio:
    def  __init__(self, status):
        self.status = status    #  0/1
'''
=======
        self.engine.start()


car = Car("Toyota", "Camry", 200)
car.start()
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3

# Car.py
from Engine import Engine  # Importing the Engine class from Engine.py       

class Car:
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)  # Composition: Engine is part of Car

    def start(self):
        print(f"{self.make} {self.model} is starting.")
        self.engine.start()


car = Car("Toyota", "Camry", 200)
car.start()
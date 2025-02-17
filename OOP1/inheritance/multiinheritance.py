class Car:
    
    def drive(self):
        return "Driving on the road"

class Plane:
    def fly(self):
        return "Flying in the sky"

#Multiple Inheritance (การสืบทอดหลายคลาสพร้อมกัน)
class FlyingCar(Car, Plane):
    def transform(self):
        return "Switching mode between driving and flying"

# การใช้งาน
flying_car = FlyingCar()
print(flying_car.drive())  # Output: Driving on the road
print(flying_car.fly())    # Output: Flying in the sky
print(flying_car.transform())  # Output: Switching mode between driving and flying

'''
print(isinstance(flying_car, Car))      # True
print(isinstance(flying_car, Plane))    # True
print(isinstance(flying_car, FlyingCar))     # True

print(issubclass(FlyingCar, Car))  # True
print(issubclass(FlyingCar, Plane))   # True
print(issubclass(Car, Plane))    # False
'''
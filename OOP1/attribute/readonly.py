class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):  # Read-Only Attribute
        return self._radius
    
    # แล้วเปลี่ยนได้ใหม   

c1 = Circle(10)
print(c1.radius)  # Output: 10
#c1.radius = 15    # Error: AttributeError
 

c2 = Circle(500)
print(c2.radius)  # Output: 10

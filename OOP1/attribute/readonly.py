class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):  # Read-Only Attribute
        return self._radius
    
    # แล้วเปลี่ยนได้ใหม   

circle = Circle(10)
print(circle.radius)  # Output: 10
circle.radius = 15    # Error: AttributeError
 

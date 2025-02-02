class Shape:
    def __init__(self):
        self.l = 0

    def getl(self):
        self.l = int(input())

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

shape = Shape()
print(f"Area of Shape: {shape.area()}")

shape.getl()
square = Square(shape.l)
print(f"Area of Square: {square.area()}")

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

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

shape = Shape()
print(f"Area of Shape: {shape.area()}")

shape.getl()
square = Square(shape.l)
print(f"Area of Square: {square.area()}")

length = int(input())
width = int(input())
rectangle = Rectangle(length, width)
print(f"Area of Rectangle: {rectangle.area()}")

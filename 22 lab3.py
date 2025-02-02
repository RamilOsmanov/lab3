import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"Point moved to: ({self.x}, {self.y})")

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


point1 = Point(3, 4)
point1.show() 

point1.move(6, 8)  
point1.show()  

point2 = Point(0, 0) 
print(f"Distance between point1 and point2: {point1.dist(point2):.2f}")

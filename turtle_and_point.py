import turtle
import matplotlib.pyplot as plt

class Polygon:
    def __init__(self, sides, name, size=100, color="black", line_thickness=1):
        self.sides = sides 
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides - 2) *180 #<- formula for the measure of an interior angle
        self.angle = self.interior_angles/self.sides 
        
    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        
class Square(Polygon):
    def __init__(self, size=100, color="black", line_thickness=1):
        super().__init__(4, "Square", size, color, line_thickness)
        
    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()
        
        
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x,y)
        
        else:
            x = self.x + other
            y = self.y + other
            return Point(x,y)
    
    def plot(self):
        plt.scatter(self.x, self.y)
        
hexagon = Polygon(4, "Hexagon", size=100)
hexagon.draw()

a = Point(4,5)
b = Point(3,3)
c = a + b
d = a + 5 + b

a.plot()
b.plot()
c.plot()
d.plot()

print(c.x, c.y)
plt.show()

square = Square(color="green", size=100)
print(square.draw())
turtle.done()
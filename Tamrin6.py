from abc import ABC, abstractmethod

class Shape(ABC):
    
    def area_calculate(self):
        pass
    
    def perimeter_calculate(self):
        pass

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area_calculate(self):
        return self.width * self.height
    
    def perimeter_calculate(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159  
    
    def area_calculate(self):
        return self.pi * self.radius * self.radius
    
    def perimeter_calculate(self):
        return 2 * self.pi * self.radius

if __name__ == "__main__":
   
    shapes_list = [
        Rectangle(5, 3),
        Circle(4)
    ]
    
    for shape in shapes_list:
        print(f"Shape: {type(shape).__name__}")
        print(f"Area: {shape.area_calculate():.2f}")
        print(f"Perimeter: {shape.perimeter_calculate():.2f}")
        print("-" * 20)

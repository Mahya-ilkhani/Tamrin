from from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def init(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def init(self, radius_value):
        self.radius_value = radius_value

    def area(self):
        return 3.14159 * self.radius_value ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius_value


shapes_list = [
    Rectangle(6, 8),
    Circle(5)
]

for shape in shapes_list:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
        print("-" * 20)

# 1.Execute
def execute(function, *args):
    return function(*args)


# 2.Instruments
def play_instrument(instrument):
    return instrument.play()


# 3.Shapes
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


# 4.ImageArea
class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()
    
    def __ge__(self, other):
        return self.get_area() >= other.get_area()
    
    def __lt__(self, other):
        return self.get_area() < other.get_area()
    
    def __le__(self, other):
        return self.get_area() <= other.get_area()
    
    def __eq__(self, other):
        return self.get_area() == other.get_area()
    
    def __ne__(self, other):
        return self.get_area() != other.get_area()


















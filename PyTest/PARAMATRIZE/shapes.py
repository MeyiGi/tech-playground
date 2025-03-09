import math 

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return (2 * self.width) + (2 * self.length)
    
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
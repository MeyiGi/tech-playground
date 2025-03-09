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
        return (self.width * 2) + (self.length * 2)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False
        
        return self.width == other.width and self.length == other.length
import shapes
import math


class TestCircle:
    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = shapes.Circle(10)
        
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle
        
    def test_area(self):
        result = self.circle.area()
        expected = math.pi * self.circle.radius ** 2
        
        assert result == expected
        
    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        
        assert result == expected
    
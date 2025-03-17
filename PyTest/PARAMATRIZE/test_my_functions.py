import shapes
import pytest


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_area(side_length, expected_area):
    assert shapes.Square(side_length=side_length).area() == expected_area
    
    
@pytest.mark.parametrize("side_length, expected_perimeter", [(5, 20), (4, 16), (3, 12)])
def test_multiple_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length=side_length).perimeter() == expected_perimeter
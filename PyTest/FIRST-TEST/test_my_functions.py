import pytest
import my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5
    
    
def test_add_strings():
    result = my_functions.add("I like", " burgers")
    assert result == "I like burgers"
    
    
def test_divide():
    result = my_functions.divide(4, 2)
    assert result == 2
    
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = my_functions.divide(10, 0)
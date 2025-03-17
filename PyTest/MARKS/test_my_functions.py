import pytest
import my_functions
import time


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5
    
    
def test_add_strings():
    result = my_functions.add("I like", " burgers")
    assert result == "I like burgers"
    
    
def test_divide():
    result = my_functions.divide(4, 2)
    assert result == 2
    
    
@pytest.mark.xfail(reason="we know number can not be divide by zero")
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = my_functions.divide(10, 0)
        

@pytest.mark.slow
def test_slow():
    time.sleep(5)
    result = my_functions.divide(4, 2)
    assert result == 2
    
    
@pytest.mark.skip(reason="this testcase is broken")
def test_skip():
    time.sleep(5)
    result = my_functions.divide(4, 2)
    assert result == 2
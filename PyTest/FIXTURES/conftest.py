import pytest
import shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)
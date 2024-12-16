# plain assert statements in pytest
# popular, flexible, integration with unittest
# automatic test detection
# parametization, fixtures

import pytest
from pytest_files.my_functions import * 

def test_answers():
    result = add(1, 2)
    assert result == 3
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# class based test

#class Test_area:
    #def setup_method(self):
     #   self.x = Area(10, 5)

    #def test_area(self):
     #   self.x.area() == 50

    #def teardown_method(self):
        #del self.x

# fixtures

#@pytest.fixture
#def x():
#    return Area(10, 5)

#def test_area(x):
#    assert x.area() == 50

# paramatisation

@pytest.mark.parametrize("length, width, area",[(5,10,50),(10,10,100),(5,5,25)])
def test_multiple_cases(length, width, area):
    x = Area(length, width)
    assert x.area() == area

@pytest.mark.skip(reason="something")
def test_skip():
    assert add(1, 2) == 3
from unit_test import squred
import pytest

def py_test_positive():
    # list1 = [2,3,-2,-3,0]
    # for i in list1:
    #     assert(0:4)
    
    assert squred(2) == 4
    assert squred(3) == 9
def py_test_negetive():    
    assert squred(-2) == 4
    assert squred(-3) == 9
def other():    
    assert squred(0) == 0
def test_str():
    with pytest.raises(TypeError):
        squred('cat')    
    
# on the cli >> 'pytest test2.py' to run the test   
# try to use a list
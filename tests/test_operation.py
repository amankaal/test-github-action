from src.math_operation import add,mul

# writing the test cases for the add function

def test_add():
    assert add(2,3) == 5  #check the add function whether the 2+3 == 5 , give true or false
    assert add(-1,1) == 0

def test_mul():
    assert mul(2,3) == 6
    assert mul(1,1) == 1
    assert mul(2,3) == 6
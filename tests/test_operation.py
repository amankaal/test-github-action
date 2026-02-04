from src.math_operation import add,mul,sub

# writing the test cases for the add function

def test_add():
    assert add(2,3) == 5  #check the add function whether the 2+3 == 5 , give true or false
    

def test_mul():
    assert mul(2,3) == 6
# new add this
def test_sub():
    assert sub(5,3) == 2
    
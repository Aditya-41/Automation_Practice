import pytest

@pytest.mark.run(order=4)
def test_m1():
    print("test_m1 is called from test 2.py")
    
@pytest.mark.run(order=3)
def test_m2():
    print("test_m2 is called from test 2.py")
    
@pytest.mark.run(order=2)
def test_m3():
    print("test_m3 is called from test 2.py")
    
@pytest.mark.run(order=1)
def test_m4():
    print("test_m4 is called from test 2.py")
    
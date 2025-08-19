

import pytest,allure


def test_m1():
    allureLogs("test_m1 is called from test 1.py")
    print("test_m1 is called from test 1.py")
    
def test_m2():
    allureLogs("test_m2 is called from test 1.py")
    print("test_m2 is called from test 1.py")

@pytest.mark.skip(reason="Skipping test_m3")
def test_m3():
    allureLogs("test_m3 is called from test 1.py")
    print("test_m3 is called from test 1.py")
    
def test_m4():
    allureLogs("test_m4 is called from test 1.py")
    allureLogs("This test is expected to fail")
    # pytest.xfail("Expected failure for demonstration purposes")
    # Uncomment the line below to simulate a failure
    # assert False, "This test is expected to fail"
    print("test_m4 is called from test 1.py")
    assert False, "This test is expected to fail"
    
def allureLogs(text):
    with allure.step(text):
        pass
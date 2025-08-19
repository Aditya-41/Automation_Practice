import pytest

@pytest.yield_fixture(scope="module", autouse=True)
def beforeClass():
    print("Setup is called before test 3.py")
    yield
    print("Teardown is called after test 3.py")
 

@pytest.yield_fixture(scope="function", autouse=True)
def beforeMethod():
    print("Setup is called before each test function in test 3.py")
    yield
    print("Teardown is called after each test function in test 3.py")
    
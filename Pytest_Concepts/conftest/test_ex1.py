
# @pytest.yield_fixture(scope="function", autouse=True)
# def aftersetUp():
#     print("Teardown is called after each test method in test 3.py")   
    
 
def test_m1(beforeMethod,beforeClass):
    print("test_m1 is called from test 1.py")
    
def test_m2(beforeMethod,beforeClass):
    print("test_m2 is called from test 1.py")
    
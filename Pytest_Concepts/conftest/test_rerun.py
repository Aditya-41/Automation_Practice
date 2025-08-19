import pytest


@pytest.mark.flaky(reruns=5, reruns_delay=1)
def test_M1():
    var1 = 10
    var2 = 20
    
    assert var1 == var2
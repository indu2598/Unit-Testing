import pytest
# Test fixtures (Pytest Feature)
@pytest.fixture()
# @pytest.fixture(autouse=True)
def setup():
    print("\n Setup Excecutng")

def test1():
    print("Test 1 Exceuting")
    assert True

def test2():
    print("Test 2 Exceuting")
    assert True

def test3(setup):
    print("Test 3 Exceuting")
    assert True

@pytest.mark.usefixtures("setup")
def test4():
    print("Test 4 Exceuting")
    assert True
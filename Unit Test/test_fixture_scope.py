""" Test Fixtures Scope :
- it has four different scope
1.function : run once for each test
2. Class - Run the fixture once for each class
3. Module - Run the fixture when module goes in scope
4. Session - The fixture is run when pytest start
"""


import pytest

@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\n Setup Session")

@pytest.fixture(scope="module", autouse=True)
def setupSession2():
    print("\n Setup Module")

@pytest.fixture(scope="function", autouse=True)
def setupSession3():
    print("\n Setup Function")

def test1():
    print("Test1")
    assert True

def test2():
    print("test2")
    assert True

# For class based Test
@pytest.fixture(scope="class", autouse=True)
def setupSession3():
    print("\n Setup Class")

@pytest.fixture(scope="module", autouse=True)
def setupSession4():
    print("\n Setup Module")

@pytest.fixture(scope="function", autouse=True)
def setupSession5():
    print("\n Setup Function")

class TestClass:
    def test1(self):
        print("Test 1 ")
        assert True
    def test2(self):
        print('Test 2')
        assert True

# pytest fixture with param
#  this setup is called for each value in param
@pytest.fixture(params=[2,4,5])
def setupMethod(request):
    val = request.params
    return val

def test5(setupMethod):
    print(setupMethod)
    assert True
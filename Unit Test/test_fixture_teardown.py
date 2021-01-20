import pytest

# with yield keyword

@pytest.fixture()
def setup():
    print("Setup Excecuting")
    yield
    print("TearDown Executing")
@pytest.fixture(autouse=True)
def setup2(request):
    print("Setup Function without yield")
    def teardown_a():
        print("Teardown A")
    def teardown_b():
        print("Teardown B")
    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)
def test1(setup):
    print("Test1 Executing!")
    assert True

def test2():
    print('Test2 Exceuting')
    assert True

""" Test Fixtures Scope :
- it has four different scope
1.function : run once for each test
2. Class - Run the fixture once for each class
3. Module - Run the fixture when module goes in scope
4. Session - The fixture is run when pytest start 
"""
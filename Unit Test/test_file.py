# -----------------------Coming from UnitTest and nose Background and supported by pytest --------------
# setup functions are called before each test runs
def setup_function(function):
    if function == test1:
        print("\nSetup in test1")
    elif function == test2:
        print("\nsetup test2")
    else:
        print("setting up unknown function")

# these teardown function runs after each test case runs
def teardown_function(function):
    if function == test1:
        print("\nteardown test1 ")
    elif function == test2:
        print("\nteardown test2")
    else:
        print("tear down unkown function")

#  now setting up setup module and teardown module
def setup_module(module):
    print("\n \n Setup Module ")
def teardown_module(module):
    print("\n Teardown Module ")
def test1():
    print("Excecuting test1")
    assert True

def test2():
    print("Executing tese 2")
    assert True


# class based SETUP and TEARDOWN method

class TestClass():
    @classmethod
    def setup_class(cls):
        print("Setup TestClass")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass")
    def setup_method(self,method):
        if method == self.test1:
            print("Setup Test1 ")
        elif method == self.test2:
            print("setup test2 ")
        else:
            print("setup unkown method")
    def teardown_method(self,method):
        if method == self.test1:
            print("Teardown test1")
        elif method == self.test2:
            print("Teardown test2")
        else:
            print("Teardown unkown method")

    def test1(self):
        print("Excecuting test1")
        assert True

    def test2(self):
        print("Executing tese 2")
        assert True


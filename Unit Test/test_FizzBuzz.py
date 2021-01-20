import pytest

def isMultiple(num , div):
    return num%div ==0
def FizzBuzz(num):
    if isMultiple(num , 3):
        if isMultiple(num, 5):
            return "FizzBuzz"
        return "Fizz"
    elif isMultiple(num ,5):
        return "Buzz"
    return str(num)

# test 1st
# def test_canFizzBuzz():
#     FizzBuzz(1)

#collection of second and third test
def checkFizzBuzz(val , returnval ):
    val = FizzBuzz(val)
    assert val== returnval

# test 2nd
def test_return1with1response():
    # val = FizzBuzz(1)
    # assert val =='1'
    checkFizzBuzz(1,'1')

# test 3rd
def test_return2with2inresponse():
    # val = FizzBuzz(2)
    # assert val=='2'
    checkFizzBuzz(2, '2')

# test 4th
def test_returnFizzwith3PassedIn():
    checkFizzBuzz(3, 'Fizz')

def test_returnBuzzwith5PassedIn():
    checkFizzBuzz(5, 'Buzz')


def test_returnFizzwith6PassedIn():
    checkFizzBuzz(6, 'Fizz')

def test_returnBuzzwith5PassedIn():
    checkFizzBuzz(10, 'Buzz')

def test_returnFizzBuzzwith15PassesIn():
    checkFizzBuzz(15, 'FizzBuzz')
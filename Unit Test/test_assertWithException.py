import pytest
from pytest import approx
from pytest import raises


def test_comapreInt():
    assert 1 ==1

def test_compareString():
    assert str == str

def test_comapareList():
    assert [2,4]==[2,4]

def test_compareFloat():
    # assert (0.1+0.2)==0.3
    assert (0.1 + 0.2) == approx(0.3)


# Check whether function is raise an error or not
def RaiseError(x):
    raise x
def test_raiseException():
    with raises(ValueError):
        RaiseError(ValueError)

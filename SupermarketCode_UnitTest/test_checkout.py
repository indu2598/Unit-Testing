from CheckOut import CheckOut
import pytest
from pytest import approx
# def test_CreateCheckoutInstance():
#     co = CheckOut()

@pytest.fixture()
def checkOut():
    co = CheckOut()
    co.addItemPrice('a', 1)
    co.addItemPrice('b', 1)
    co.addItemPrice('c', 1)
    co.addDiscount('a', 3, 2)
    return co

# def test_AddItemPrice(checkOut):
#     checkOut.addItemPrice('a',100)
#
# def test_AddItem(checkOut):
#     checkOut.AddItem('a')

# def test_canCalculateTotal(checkOut):
#     checkOut.AddItem('a')
#     assert checkOut.canCalculateTotal() == 1

def test_CaluculateTotalwithMultipleItem(checkOut):
    checkOut.AddItem('b')
    checkOut.AddItem('c')
    assert checkOut.canCalculateTotal()==2

def test_addDiscount(checkOut):
    checkOut.addDiscount('a', 3 , 2)

# @pytest.mark.skip
def test_applydiscountToTotal(checkOut):
    checkOut.addDiscount('a', 3, 2)
    checkOut.addDiscount('b', 4, 1)
    checkOut.AddItem('a')
    checkOut.AddItem('a')
    checkOut.AddItem('a')
    checkOut.AddItem('b')
    checkOut.AddItem('b')
    checkOut.AddItem('b')
    checkOut.AddItem('b')
    assert checkOut.canCalculateTotal()==3


def test_raiseExceptionforitemWithoutprice(checkOut):
    with pytest.raises(Exception):
        checkOut.AddItem(c)
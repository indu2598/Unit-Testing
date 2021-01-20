class CheckOut:
    class Discount:
        def __init__(self,n,p):
            self.noOfItem = n
            self.price = p

    def __init__(self):
        self.prices = {}
        self.discountItems = {}
        self.itemsInCart = {}
    def addItemPrice(self,item,price):
        self.prices[item] = price

    def AddItem(self,item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.itemsInCart:
            self.itemsInCart[item]+=1
        else:
            self.itemsInCart[item]= 1

    def canCalculateTotal(self):

        total = 0
        for item,count in self.itemsInCart.items():
            if item in self.discountItems:
                disc = self.discountItems[item]
                if count>=disc.noOfItem:
                    noOfdiscount = count//disc.noOfItem
                    total+=noOfdiscount*disc.price
                    remaing = count % disc.noOfItem
                    total += remaing * self.prices[item]
            else:
                total+=count*self.prices[item]
        return total

    def addDiscount(self, item , noOfItem , price):
        discount = self.Discount(noOfItem,price)
        self.discountItems[item] = discount

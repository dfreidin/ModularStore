class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, tax):
        return self.price * (1 + tax)
    def returnItem(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if reason == "like new":
            self.status = "for sale"
        if reason == "opened":
            self.status = "used"
            self.price *= 0.8
        return self
    def displayInfo(self):
        print "Price:", str(self.price)
        print "Item Name:", self.name
        print "Weight:", str(self.weight)
        print "Brand:", self.brand
        print "Status:", self.status
        return self
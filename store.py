import product

class Store(object):
    def __init__(self, address, owner):
        self.products = []
        self.location = address
        self.owner = owner
    def add_product(self, price, name, weight, brand):
        self.products.append(product.Product(price, name, weight, brand))
        return self
    def remove_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p);
        return self
    def inventory(self):
        for p in self.products:
            p.displayInfo()
        return self

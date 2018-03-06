import product
import store

s = store.Store("123 main st", "David")
s.add_product(100, "Computer", 4, "Dell")
s.add_product(200, "Apple", 50, "Apple")
s.inventory()
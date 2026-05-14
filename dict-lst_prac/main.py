from cart import Cart
from product import Product

cart = Cart()
item_1 = Product("Apple", 2)

cart.add_to_cart(item_1)

print(cart)

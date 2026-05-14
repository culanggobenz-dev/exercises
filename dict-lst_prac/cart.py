from product import Product

class Cart:
    def __init__(self):
        self.__cart = []
    
    def add_to_cart(self, product):
        if not isinstance(product, Product):
            return f"{self.__cart}: {product} is not in acceptable format."
        self.__cart.append(product.product_info)

    def __str__(self):
        return f"Items in cart:\n{self.__cart}"
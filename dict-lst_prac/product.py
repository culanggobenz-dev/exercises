class Product:
    def __init__(self, name : str, price : int = 0):
        self.__product_info = {}
        self.__name = name
        self.__price = price

    @property
    def product_info(self):
        return self.__product_info
    
    @product_info.setter
    def product_info(self, value):
        self.__product_info = value
    
    def pick_product(self, name, price):
        self.__product_info["item"] = name
        self.__product_info["price"] = price
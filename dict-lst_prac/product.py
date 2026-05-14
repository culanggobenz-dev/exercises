class Product:
    def __init__(self, name : str, price : int = 0):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    def __str__(self):
        return f"{self.__name} : ${self.__price}"
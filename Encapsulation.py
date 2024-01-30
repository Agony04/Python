# Bir değişkene ya da metoda erişimi sınırlandırmak için kullanılır.

class Phone:
    def __init__(self):
        self.brand = "Apple"
        self.__price = 1000 # Encapsulation via "__"

    def sell(self):
        print("Price: {}".format(self.__price))

    def sellPrice(self, price):
        self.__price = price
        print("Price: {}".format(self.__price))


obj = Phone()
obj.sell()
obj.__price = 1100
obj.sellPrice(1100)

# Built-in function

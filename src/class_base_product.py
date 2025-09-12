from abc import ABC, abstractmethod

class BaseProduct(ABC):

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass



class MixinPrint:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self, name, description, price, quantity):
        print(f"{name}, {description}, {price}, {quantity}")

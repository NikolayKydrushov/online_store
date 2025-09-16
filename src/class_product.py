from src.class_base_product import BaseProduct, MixinPrint

class Product(BaseProduct, MixinPrint):
    # __slots__ = ('name', 'description', 'price', 'quantity')

    # name: str  # название
    # description: str  # описание
    # __price: float  # цена
    # quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        # self.name = name
        # self.description = description
        # self.__price = price
        # self._MixinPrint__price = self.__price
        # self.quantity = quantity
        # super().__init__()
        # print(repr(self))

    # метод вывода информации о продукте
    def __str__(self):
        return f"{self.name}, {self.price:.2f} руб., остаток: {self.quantity} шт."

     # метод подсчета суммарной стоимости передаваемых товаров
    def __add__(self, other):
        if type(self) == type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            return TypeError

    # класс-метод принимающий на вход параметры товара в словаре и возвращать созданный объект Product
    @classmethod
    def new_product(clc, prod):
        return clc(prod["name"], prod["description"], prod["price"], prod["quantity"])

    # геттер для цены
    @property
    def price(self):
        return self._BaseProduct__price

    # сеттер для проверки корректности цены
    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._BaseProduct__price = value

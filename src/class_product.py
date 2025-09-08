class Product:
    name: str  # название
    description: str  # описание
    __price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    # класс-метод принимающий на вход параметры товара в словаре и возвращать созданный объект Product
    @classmethod
    def new_product(clc, prod):
        return clc(prod["name"], prod["description"], prod["price"], prod["quantity"])

    # геттер для цены
    @property
    def price(self):
        return self.__price

    # сеттер для проверки корректности цены
    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

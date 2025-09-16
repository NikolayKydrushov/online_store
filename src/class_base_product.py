from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self, name, description, price, quantity):
        """
        Конструктор для базового класса продуктов.

        name: название
        description: описание
        quantity: количество в наличии
        """
        self.name = name
        self.description = description
        self._BaseProduct__price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        """Метод вывода информации о продукте"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Метод подсчета суммарной стоимости передаваемых товаров"""
        pass

    # класс-метод принимающий на вход параметры товара в словаре и возвращать созданный объект Product
    @classmethod
    @abstractmethod
    def new_product(clc, args, **kwargs):
        """Метод создания нового объекта продукта из словаря"""
        pass

    # геттер для цены
    @property
    @abstractmethod
    def price(self):
        """Метод возвращает цену продукта"""
        pass

    # сеттер для проверки корректности цены
    @price.setter
    @abstractmethod
    def price(self, value):
        """Метод для установки новой цены"""
        pass


# class MixinPrint:
#     """Миксин для вывода сообщений о создании объекта"""
#
#     def __init__(self, name, description, price, quantity):
#         MixinPrint.__repr__(self)
#         super().__init__(name, description, price, quantity)
#
#     def __repr__(self):
#         return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"


class MixinPrint:
    """Миксин для вывода сообщений о создании объекта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"
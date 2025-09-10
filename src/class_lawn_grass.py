from src.class_product import Product


class LawnGrass(Product):
    country: str  # страна-производитель
    germination_period: str  # срок прорастания
    color: str  # цвет

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

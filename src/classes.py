class Product:
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str  # название
    description: str  # описание
    products: list  # список товаров категории

    number_categories = 0  # количество категорий
    numbers_products = 0  # количество товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.numbers_products = len(self.products)
        if Category.numbers_products != 0:
            Category.number_categories += 1


# prod_1 = Product("", "", 0, 0)
# prod_2 = Product("", "", 0, 0)
# prod_3 = Product("", "", 0, 0)
#
# category_1 = Category("", "", [])
# category_2 = Category("", "", [])
# category_3 = Category("", "", [])

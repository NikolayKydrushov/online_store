class Category:
    name: str  # название
    description: str  # описание
    __products: list  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.product_count += len(self.__products)
        Category.category_count += 1

    # метод добавления нового продукта
    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    # геттер для вывода списка товаров
    @property
    def products(self):
        result = []

        for product in self.__products:
            result.append(
                f"{product.name}, {product.price:.2f} руб., остаток: {product.quantity} шт."
            )
        return "\n".join(result)

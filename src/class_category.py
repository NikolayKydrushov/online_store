from src.class_product import Product


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

    # метод вывода названия категории и общее кол-во товаров в данной категории
    def __str__(self):
        total_number_products = 0

        for i in self.__products:
            total_number_products += i.quantity

        return f"{self.name}, количество продуктов: {total_number_products} шт."

    # метод добавления нового продукта
    def add_product(self, product):
        if isinstance(product, Product):
            if issubclass(type(product), Product):
                self.__products.append(product)
                Category.product_count += 1
        else:
            raise TypeError

    # геттер для вывода списка товаров
    @property
    def products(self):
        result = []

        for product in self.__products:
            result.append(
                f"{product.name}, {product.price:.2f} руб., остаток: {product.quantity} шт."
            )
        return "\n".join(result)


    # метод подсчитывающий средний ценник всех товаров
    def middle_price(self):
        try:
            if not self.__products:
                # исключение в случаи отсутствия в категории нет товаров
                raise CategoryWithoutProducts("В данном классе нет продуктов")

            total_number_products = sum(i.quantity for i in self.__products)
            total_price_products = sum(i.price for i in self.__products)

            price_middle = total_price_products / total_number_products
            return round(price_middle, 2)

        except CategoryWithoutProducts:
            return 0
        # исключение в случаи деления на 0
        except ZeroDivisionError:
            return 0



class CategoryWithoutProducts(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "В данном классе нет продуктов"

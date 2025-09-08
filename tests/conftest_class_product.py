import pytest

from src.class_product import Product


# 1. Фикстура для пустого объекта класса Product
@pytest.fixture()
def product_empty():
    return Product("", "", 0, 0)


# 2. Фикстура для объекта класса Product
@pytest.fixture
def product_init():
    return Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 10000.5, 2
    )


# 3. Фикстура для добавления нового продукта, геттера и сеттера
@pytest.fixture
def product_new():
    prod_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14,
    }
    product = Product.new_product(prod_data)
    return product

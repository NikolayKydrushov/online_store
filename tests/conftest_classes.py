import pytest

from src.classes import Category, Product


# 1. Фикстура для пустого объекта класса Category
@pytest.fixture
def category_empty():
    return Category("", "", [])


# 2. Фикстура для объекта класса Category
@pytest.fixture
def category_init():
    return Category("Коты", "Прекрасные существа", ["Египетская", "Московская"])


# 1. Фикстура для пустого объекта класса Product
@pytest.fixture()
def product_empty():
    return Product("", "", 0, 0)


# 2. Фикстура для объекта класса Product
@pytest.fixture
def product_init():
    return Product(
        "Клеопатра", "Если у вас аллергия на шерсть - это ваш выбор", 10000.5, 2
    )

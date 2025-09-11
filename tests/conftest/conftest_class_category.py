import pytest

from src.class_category import Category


# 1. Фикстура для пустого объекта класса Category
@pytest.fixture
def category_empty():
    return Category("", "", [])


# 2. Фикстура для объекта класса Category
@pytest.fixture
def category_init():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций",
        [],
    )

from src.classes import Category
from tests.conftest_classes import (category_empty, category_init, product_empty,
                                    product_init)

# Тесты для класса Category


# Тест №2 инициализация пустых атрибутов
def test_init_empty_category(category_empty):
    assert category_empty.name == ""
    assert category_empty.description == ""
    assert category_empty.products == []
    assert Category.number_categories == 1
    assert Category.numbers_products == 0


# Тест №2 инициализация атрибутов
def test_init_category(category_init):
    assert category_init.name == "Коты"
    assert category_init.description == "Прекрасные существа"
    assert category_init.products == ["Египетская", "Московская"]
    assert Category.number_categories == 2
    assert Category.numbers_products == 2


# Тесты для класса Product


# Тест №1 инициализация пустых атрибутов
def test_init_empty_product(product_empty):
    assert product_empty.name == ""
    assert product_empty.description == ""
    assert product_empty.price == 0
    assert product_empty.quantity == 0


# Тест №2 инициализация атрибутов
def test_init_product(product_init):
    assert product_init.name == "Клеопатра"
    assert product_init.description == "Если у вас аллергия на шерсть - это ваш выбор"
    assert product_init.price == 10000.5
    assert product_init.quantity == 2

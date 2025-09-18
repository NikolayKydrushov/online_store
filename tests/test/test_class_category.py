import pytest

from src.class_category import Category, CategoryWithoutProducts
from tests.conftest.conftest_class_category import category_empty, category_init
from tests.conftest.conftest_class_product import product_init, product_new

# Тесты для класса Category


# Тест №1 инициализация пустых атрибутов
def test_init_empty_category(category_empty):
    assert category_empty.name == ""
    assert category_empty.description == ""
    assert category_empty.products == ""
    assert Category.category_count == 1
    assert Category.product_count == 0


# Тест №2 инициализация атрибутов
def test_init_category(category_init):
    assert category_init.name == "Смартфоны"
    assert (
        category_init.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций"
    )
    assert category_init.products == ""
    assert Category.category_count == 2
    assert Category.product_count == 0


# Тест №3 добавление новых продуктов в категории
def test_add_product(product_init, product_new, category_init):
    category = Category("Смартфоны", "Смартфоны - средство коммуникации")

    category.add_product(product_init)
    assert Category.product_count == 1  # Один товар добавлен
    assert len(category._Category__products) == 1  # Один элемент в списке товаров
    assert Category.category_count == 4  # Кол-во категорий

    category.add_product(product_new)
    assert Category.product_count == 2  # Товар добавлен
    assert len(category._Category__products) == 2  # Один элемент в списке товаров
    assert Category.category_count == 4 # Кол-во категорий

    with pytest.raises(TypeError):
        category.add_product(category_init)


# Тест №4 работа метода str
def test_str_category(product_init, product_new):
    category = Category(
        "Смартфоны", "Смартфоны - средство коммуникации", [product_init, product_new]
    )
    assert str(category) == "Смартфоны, количество продуктов: 16 шт."

    # тест при добавлении новых товаров
    category.add_product(product_new)
    assert str(category) == "Смартфоны, количество продуктов: 30 шт."


# Тест №5 работа метода str без передачи товаров
def test_empty_str_category(product_init, product_new):
    category = Category("Нет категории", "")
    assert str(category) == "Нет категории, количество продуктов: 0 шт."


def test_exception_on_empty_category():
    cat = Category("Смартфоны",
                   "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций",
        [])
    assert cat.middle_price() == 0

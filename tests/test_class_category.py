from src.class_category import Category
from src.class_product import Product
from tests.conftest_class_category import category_empty, category_init

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
def test_add_product():
    category = Category("Смартфоны", "Смартфоны - средство коммуникации")
    product = Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    category.add_product(product)
    assert Category.product_count == 1  # Один товар добавлен
    assert len(category._Category__products) == 1  # Один элемент в списке товаров
    assert Category.category_count == 3  # Категорий одна

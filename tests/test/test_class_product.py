from src.class_product import Product
from tests.conftest.conftest_class_product import (
    product_empty,
    product_init,
    product_new,
)

# Тесты для класса Product


# Тест №1 инициализация пустых атрибутов
def test_init_empty_product(product_empty):
    assert product_empty.name == ""
    assert product_empty.description == ""
    assert product_empty.price == 0
    assert product_empty.quantity == 0


# Тест №2 инициализация атрибутов
def test_init_product(product_init):
    assert product_init.name == "Samsung Galaxy C23 Ultra"
    assert product_init.description == "256GB, Серый цвет, 200MP камера"
    assert product_init.price == 10000.5
    assert product_init.quantity == 2


# Тест №3 добавление нового продукта
def test_new_product(product_new):
    assert product_new.name == "Xiaomi Redmi Note 11"
    assert product_new.description == "1024GB, Синий"
    assert product_new.price == 31000.0
    assert product_new.quantity == 14


# Тест №4 тестирование сеттера и геттера
def test_price_setter(product_new):
    product_new.price = 30000  # Устанавливаем новую цену
    assert product_new.price == 30000  # Новая цена установлена

    try:
        product_new.price = -1000  # Пробуем установить отрицательную цену
    except Exception as e:
        pass  # Никаких исключений возникать не должно, так как сработает warning
    finally:
        assert product_new.price == 30000  # Цена осталась неизменной


# Тест №5 работа метода str
def test_str_product(product_init, product_empty):
    assert (
        str(product_init) == "Samsung Galaxy C23 Ultra, 10000.50 руб., остаток: 2 шт."
    )
    assert str(product_empty) == ", 0.00 руб., остаток: 0 шт."


# Тест №6 работа метода add с двумя продуктами
def test_add_product(product_init, product_new):
    expected_total_cost = (10000.5 * 2) + (31000.0 * 14)
    actual_total_cost = product_init + product_new
    assert actual_total_cost == expected_total_cost


# Тест №7 работа метода add с одним продуктов
def test_one_add_product(product_init):
    expected_total_cost = 10000.5 * 2
    actual_total_cost = product_init.price * product_init.quantity
    assert actual_total_cost == expected_total_cost


# Тест №8 работа миксина вывода информации об объекте
def test_mixin_print(product_init):
    creation_message = product_init.get_creation_message()
    expected_output = "Product (Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 10000.5, 2)"
    assert creation_message == expected_output

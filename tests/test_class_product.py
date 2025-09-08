from tests.conftest_class_product import (product_empty, product_init,
                                          product_new)

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

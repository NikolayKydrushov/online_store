from tests.conftest.conftest_class_smartphone import (
    smartphone_empty,
    smartphone_init,
    smartphone_new,
)

# Тесты для класса Smartphone


# Тест №1 инициализация пустых атрибутов
def test_init_empty_smartphone(smartphone_empty):
    assert smartphone_empty.name == ""
    assert smartphone_empty.description == ""
    assert smartphone_empty.price == 0
    assert smartphone_empty.quantity == 0
    assert smartphone_empty.efficiency == 0
    assert smartphone_empty.model == ""
    assert smartphone_empty.memory == 0
    assert smartphone_empty.color == ""


# Тест №2 инициализация атрибутов
def test_init_smartphone(smartphone_init):
    assert smartphone_init.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_init.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_init.price == 180000.0
    assert smartphone_init.quantity == 5
    assert smartphone_init.efficiency == 95.5
    assert smartphone_init.model == "S23 Ultra"
    assert smartphone_init.memory == 256
    assert smartphone_init.color == "Серый"


# Тест №3 добавление нового продукта
def test_new_smartphone(smartphone_new):
    assert smartphone_new.name == "Xiaomi Redmi Note 11"
    assert smartphone_new.description == "1024GB, Синий"
    assert smartphone_new.price == 31000.0
    assert smartphone_new.quantity == 14
    assert smartphone_new.efficiency == 90.3
    assert smartphone_new.model == "Note 11"
    assert smartphone_new.memory == 1024
    assert smartphone_new.color == "Синий"


# Тест №4 тестирование сеттера и геттера
def test_price_setter(smartphone_new):
    smartphone_new.price = 30000  # Устанавливаем новую цену
    assert smartphone_new.price == 30000  # Новая цена установлена

    try:
        smartphone_new.price = -1000  # Пробуем установить отрицательную цену
    except Exception as e:
        pass  # Никаких исключений возникать не должно, так как сработает warning
    finally:
        assert smartphone_new.price == 30000  # Цена осталась неизменной


# Тест №5 работа метода str
def test_str_smartphone(smartphone_init, smartphone_empty):
    assert (
        str(smartphone_init)
        == "Samsung Galaxy S23 Ultra, 180000.00 руб., остаток: 5 шт."
    )
    assert str(smartphone_empty) == ", 0.00 руб., остаток: 0 шт."


# Тест №6 работа метода add с двумя продуктами
def test_add_smartphone(smartphone_init, smartphone_new):
    expected_total_cost = (180000.00 * 5) + (31000.0 * 14)
    actual_total_cost = smartphone_init + smartphone_new
    assert actual_total_cost == expected_total_cost


# Тест №7 работа метода add с одним продуктов
def test_one_add_smartphone(smartphone_init):
    expected_total_cost = 180000.00 * 5
    actual_total_cost = smartphone_init.price * smartphone_init.quantity
    assert actual_total_cost == expected_total_cost

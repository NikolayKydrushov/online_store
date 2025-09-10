from tests.conftest.conftest_class_lawn_grass import (lawn_grass_empty,
                                                      lawn_grass_init,
                                                      lawn_grass_new)

# Тесты для класса LawnGrass


# Тест №1 инициализация пустых атрибутов
def test_init_empty_lawn_grass(lawn_grass_empty):
    assert lawn_grass_empty.name == ""
    assert lawn_grass_empty.description == ""
    assert lawn_grass_empty.price == 0
    assert lawn_grass_empty.quantity == 0
    assert lawn_grass_empty.country == ""
    assert lawn_grass_empty.germination_period == ""
    assert lawn_grass_empty.color == ""


# Тест №2 инициализация атрибутов
def test_init_lawn_grass(lawn_grass_init):
    assert lawn_grass_init.name == "Газонная трава"
    assert lawn_grass_init.description == "Элитная трава для газона"
    assert lawn_grass_init.price == 500.0
    assert lawn_grass_init.quantity == 20
    assert lawn_grass_init.country == "Россия"
    assert lawn_grass_init.germination_period == "7 дней"
    assert lawn_grass_init.color == "Зеленый"


# Тест №3 добавление нового продукта
def test_new_lawn_grass(lawn_grass_new):
    assert lawn_grass_new.name == "Газонная трава 2"
    assert lawn_grass_new.description == "Выносливая трава"
    assert lawn_grass_new.price == 450.0
    assert lawn_grass_new.quantity == 15
    assert lawn_grass_new.country == "США"
    assert lawn_grass_new.germination_period == "5 дней"
    assert lawn_grass_new.color == "Темно-зеленый"


# Тест №4 тестирование сеттера и геттера
def test_price_setter(lawn_grass_new):
    lawn_grass_new.price = 30000  # Устанавливаем новую цену
    assert lawn_grass_new.price == 30000  # Новая цена установлена

    try:
        lawn_grass_new.price = -1000  # Пробуем установить отрицательную цену
    except Exception as e:
        pass  # Никаких исключений возникать не должно, так как сработает warning
    finally:
        assert lawn_grass_new.price == 30000  # Цена осталась неизменной


# Тест №5 работа метода str
def test_str_lawn_grass(lawn_grass_init, lawn_grass_empty):
    assert str(lawn_grass_init) == "Газонная трава, 500.00 руб., остаток: 20 шт."
    assert str(lawn_grass_empty) == ", 0.00 руб., остаток: 0 шт."


# Тест №6 работа метода add с двумя продуктами
def test_add_lawn_grass(lawn_grass_init, lawn_grass_new):
    expected_total_cost = (500.00 * 20) + (450.0 * 15)
    actual_total_cost = lawn_grass_init + lawn_grass_new
    assert actual_total_cost == expected_total_cost


# Тест №7 работа метода add с одним продуктов
def test_one_add_lawn_grass(lawn_grass_init):
    expected_total_cost = 500.00 * 20
    actual_total_cost = lawn_grass_init.price * lawn_grass_init.quantity
    assert actual_total_cost == expected_total_cost

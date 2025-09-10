import pytest

from src.class_smartphone import Smartphone


# 1. Фикстура для пустого объекта класса Product
@pytest.fixture()
def smartphone_empty():
    return Smartphone("", "", 0, 0, 0, "", 0, "")


# 2. Фикстура для объекта класса Product
@pytest.fixture
def smartphone_init():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


# 3. Фикстура для добавления нового продукта, геттера и сеттера
@pytest.fixture
def smartphone_new():
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )

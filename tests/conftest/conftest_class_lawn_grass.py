import pytest

from src.class_lawn_grass import LawnGrass


# 1. Фикстура для пустого объекта класса Product
@pytest.fixture()
def lawn_grass_empty():
    return LawnGrass("", "", 0, 0, "", "", "")


# 2. Фикстура для объекта класса Product
@pytest.fixture
def lawn_grass_init():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


# 3. Фикстура для добавления нового продукта, геттера и сеттера
@pytest.fixture
def lawn_grass_new():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

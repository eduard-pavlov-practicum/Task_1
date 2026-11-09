import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.burger import Burger
from constants.bun import bun_name, bun_price
from constants.ingridient import ingridient_name, ingridient_type, ingridient_price


@pytest.fixture
def bun_() -> Bun:
    return Bun(bun_name, bun_price)


@pytest.fixture
def ingredient_() -> Ingredient:
    return Ingredient(ingridient_type, ingridient_name, ingridient_price)


@pytest.fixture
def db() -> Database:
    return Database()


@pytest.fixture
def burger():
    """Фикстура для создания свежего объекта бургера перед каждым тестом."""
    return Burger()

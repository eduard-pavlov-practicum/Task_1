import pytest
from bun import Bun
from ingredient import Ingredient
from constants.bun import bun_name, bun_price
from constants.ingridients import ingridient_name, ingridient_type, ingridient_price


@pytest.fixture
def bun_() -> Bun:
    return Bun(bun_name, bun_price)


@pytest.fixture
def ingredient_() -> Ingredient:
    return Ingredient(ingridient_type, ingridient_name, ingridient_price)

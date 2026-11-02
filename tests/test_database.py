import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestsDatabase:
    def test_available_buns_returns_all_three_buns(self, db):

        buns = db.available_buns()

        assert len(buns) == 3

    def test_available_ingredients_returns_all_six_ingredients(self, db):

        ingredients = db.available_ingredients()

        assert len(ingredients) == 6

    def test_available_buns_returns_all_buns_correct_type(self, db):
        buns = db.available_buns()

        for bun in buns:
            assert isinstance(
                bun, Bun), f"Элемент {bun} не является объектом класса Bun"

    def test_available_ingredients_returns_all_ingredients_correct_type(self, db):
        ingredients = db.available_ingredients()

        for ingredient in ingredients:
            assert isinstance(
                ingredient, Ingredient), f"Элемент {ingredient} не является объектом класса Ingredient"

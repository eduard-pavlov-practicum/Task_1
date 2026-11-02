import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurgers:
    def test_set_buns_sets_bun_correctly(self, burger):
        """Позитивный: Установка булочки сохраняет объект в атрибуте bun."""
        mock_bun = Mock(spec=Bun)
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_single_item(self, burger):
        """Позитивный: Добавление одного ингредиента в пустой список."""
        mock_ing = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ing)
        assert burger.ingredients == [mock_ing]

    def test_add_multiple_ingredients_maintains_order(self, burger):
        """Позитивный: Добавление нескольких ингредиентов сохраняет порядок поступления."""
        mock_ing_1 = Mock(spec=Ingredient)
        mock_ing_2 = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)

        assert burger.ingredients == [mock_ing_1, mock_ing_2]

    @pytest.mark.parametrize("index_to_remove, expected_index", [(0, 1), (1, 0)])
    def test_remove_ingredient_removes_correct_item(self, burger, index_to_remove, expected_index):
        """Позитивный/Граничный: Удаление ингридиента с начала и с конца списка."""
        mock_ing_0 = Mock(spec=Ingredient)
        mock_ing_1 = Mock(spec=Ingredient)
        burger.ingredients = [mock_ing_0, mock_ing_1]

        expected_item = burger.ingredients[expected_index]

        burger.remove_ingredient(index_to_remove)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == expected_item

    @pytest.mark.parametrize("invalid_index", [-5, 0, 3])
    def test_remove_ingredient_invalid_index_raises_error(self, burger, invalid_index):
        """Негативный: Удаление по несуществующему индексу вызывает IndexError."""
        burger.ingredients = [Mock(spec=Ingredient), Mock(spec=Ingredient)]

        if invalid_index == 0:
            burger.ingredients = []  # Очищаем для проверки удаления из пустого списка

        with pytest.raises(IndexError):
            burger.remove_ingredient(invalid_index)

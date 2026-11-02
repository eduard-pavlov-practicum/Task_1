import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from mocks.ingredient import mock_cheese, mock_cutlet, mock_sauce
from mocks.bun import mock_bun
from constants.bun import bun_name, bun_price


class TestBurgers:
    def test_set_buns_sets_bun_correctly(self, burger):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_single_item(self, burger):
        mock_ing = mock_sauce
        burger.add_ingredient(mock_ing)
        assert burger.ingredients == [mock_ing]

    def test_add_multiple_ingredients_save_order(self, burger):

        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_cutlet)

        assert burger.ingredients == [mock_sauce, mock_cutlet]

    @pytest.mark.parametrize("index_to_remove, expected_index", [(0, 1), (1, 0)])
    def test_remove_ingredient_removes_correct_item(self, burger, index_to_remove, expected_index):
        burger.ingredients = [mock_sauce, mock_cutlet]

        expected_item = burger.ingredients[expected_index]

        burger.remove_ingredient(index_to_remove)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == expected_item

    @pytest.mark.parametrize("invalid_index", [-5, 0, 3])
    def test_remove_ingredient_invalid_index_raises_error(self, burger, invalid_index):
        burger.ingredients = [mock_sauce, mock_cutlet]

        if invalid_index == 0:
            burger.ingredients = []  # Очищаем для проверки удаления из пустого списка

        with pytest.raises(IndexError):
            burger.remove_ingredient(invalid_index)

    @pytest.mark.parametrize(
        "start_index, new_index, expected_order",
        [
            (0, 1, ["sauce", "cutlet", "cheese"]),
            (2, 0, ["cheese", "cutlet", "sauce"]),
            (1, 1, ["cutlet", "sauce", "cheese"]),
        ]
    )
    def test_move_ingredient_change_positions_correctly(self, burger, start_index, new_index, expected_order):

        burger.ingredients = [mock_cutlet, mock_sauce, mock_cheese]

        burger.move_ingredient(start_index, new_index)

        actual_order = [ing.get_name() for ing in burger.ingredients]
        assert actual_order == expected_order

    @pytest.mark.parametrize("invalid_start_index", [-10, 10])
    def test_move_ingredient_invalid_start_index_raises_error(self, burger, invalid_start_index):

        burger.ingredients = [mock_cutlet, mock_sauce]

        with pytest.raises(IndexError):
            burger.move_ingredient(invalid_start_index, 0)

    def test_get_price_with_multiple_ingredients_returns_correct_price(self, burger):

        burger.bun = mock_bun
        burger.ingredients = [mock_cutlet, mock_sauce]

        # Ожидаем: 1255*2 + 60 + 40 = 2610
        assert burger.get_price() == 2610

    def test_get_price_with_zero_ingredients_returns_only_buns_price(self, burger):

        burger.bun = mock_bun

        assert burger.get_price() == 2510

    def test_get_price_without_bun_raises_error(self, burger):
        burger.ingredients = [mock_sauce]

        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_format_with_ingredients(self, burger):

        burger.bun = mock_bun
        burger.ingredients = [mock_cutlet]

        expected_receipt = (
            f"(==== {bun_name} ====)\n"
            f"= filling cutlet =\n"
            f"(==== {bun_name} ====)\n\n"
            "Price: 2570.0"
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_format_empty_ingredients(self, burger):
        """Граничный: Чек для бургера без ингредиентов (только булка)."""

        burger.bun = mock_bun

        expected_receipt = (
            f"(==== {bun_name} ====)\n"
            f"(==== {bun_name} ====)\n\n"
            f"Price: 2510.0"
        )

        assert burger.get_receipt() == expected_receipt

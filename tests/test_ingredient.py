import pytest
from constants.ingridient import ingridient_name, ingridient_type, ingridient_price


class TestIngridient:

    def test_get_type_returns_correct_type(self, ingredient_):
        assert ingredient_.get_type() == ingridient_type

    def test_get_name_returns_correct_name(self, ingredient_):
        assert ingredient_.get_name() == ingridient_name

    def test_get_price_returns_correct_price(self, ingredient_):
        assert ingredient_.get_price() == ingridient_price

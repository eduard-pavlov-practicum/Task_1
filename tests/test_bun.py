import pytest
from constants.bun import bun_name, bun_price


class TestBun:

    def test_get_name_returns_correct_name(self, bun_):
        assert bun_.get_name() == bun_name

    def test_get_price_returns_correct_price(self, bun_):
        assert bun_.get_price() == bun_price

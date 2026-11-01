import pytest
from bun import Bun
from constants.bun import bun_name, bun_price


@pytest.fixture
def bun_() -> Bun:
    return Bun(bun_name, bun_price)

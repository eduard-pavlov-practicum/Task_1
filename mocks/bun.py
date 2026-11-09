from unittest.mock import Mock
from praktikum.bun import Bun
from constants import bun

mock_bun = Mock(spec=Bun)
mock_bun.get_name.return_value = bun.bun_name
mock_bun.get_price.return_value = bun.bun_price

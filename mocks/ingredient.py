from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING

mock_cutlet = Mock(spec=Ingredient)
mock_cutlet.get_name.return_value = "cutlet"
mock_cutlet.get_price.return_value = 60.0
mock_cutlet.get_type.return_value = INGREDIENT_TYPE_FILLING

mock_sauce = Mock(spec=Ingredient)
mock_sauce.get_name.return_value = "sauce"
mock_sauce.get_price.return_value = 40.0

mock_cheese = Mock(spec=Ingredient)
mock_cheese.get_name.return_value = "cheese"

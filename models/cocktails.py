from enum import Enum
from typing import Optional

from pydantic import BaseModel

from models.liquors import Liquor, NonLiquor


class Glass(str, Enum):
    COUPE = "Coupe"
    MARTINI = "Martini"
    ROCKS = "Rocks"
    PINT = "Pint"
    HIGHBALL = "Highball"


class Ice(str, Enum):
    NONE = "None"
    ROCKS = "Rocks"
    CUBE = "Cube"
    PEBBLE = "Pebble"
    CRUSHED = "Crushed"


class Mixing(str, Enum):
    SHAKE = "Shake"
    STIR = "Stir"


class Ingredient(BaseModel):
    is_liquor: bool
    liquor_type: Optional[Liquor] = None
    non_liquor_type: Optional[NonLiquor] = None
    quantity: float


class Cocktail(BaseModel):
    ingredients: list[Ingredient]
    mixing: Mixing
    ice: Ice
    glass: Glass


if __name__ == "__main__":
    sample1 = {
        "ingredients": [
            {
                "is_liquor": True,
                "liquor_type": {
                    "name": "Tanquery",
                    "spirit": "Gin",
                    "subtype": "London Dry",
                },
                "quantity": 2,
            },
            {
                "is_liquor": False,
                "non_liquor_type": {
                    "name": "Dry Vermouth",
                    "type": "Vermouth",
                },
                "quantity": 0.5,
            },
        ],
        "mixing": "Stir",
        "ice": "None",
        "glass": "Coupe",
    }
    cocktail1 = Cocktail.model_validate(sample1)
    print(cocktail1)

from enum import Enum
from typing import Optional

from pydantic import BaseModel

from models.liquors import Spirit, Subtype


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


class LiquorIngredient(BaseModel):
    spirit: Spirit
    subtype: Optional[Subtype] = None
    name: Optional[str] = None


class NonLiquorIngredient(BaseModel):
    name: str


class Ingredient(BaseModel):
    isLiquor: bool
    liquorType: Optional[LiquorIngredient] = None
    nonLiquorType: Optional[NonLiquorIngredient] = None
    quantity: float
    units: Optional[str] = None


class Cocktail(BaseModel):
    name: str
    description: Optional[str] = None
    ingredients: list[Ingredient]
    mixing: Mixing
    ice: Ice
    glass: Glass
    garnish: Optional[str] = None


class RecipeBook(BaseModel):
    allCocktails: list[Cocktail]


if __name__ == "__main__":
    sample1 = {
        "name": "Dry Martini",
        "ingredients": [
            {
                "isLiquor": True,
                "liquorType": {
                    "spirit": "Gin",
                    "subtype": "London Dry",
                },
                "quantity": 2,
            },
            {
                "isLiquor": False,
                "nonLiquorType": {
                    "name": "Dry Vermouth",
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

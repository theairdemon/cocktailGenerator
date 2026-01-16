import json
from pathlib import Path

from models.cocktails import Cocktail, Ice, LittleBlackBook
from pydantic import ValidationError


def build_cocktail_book() -> LittleBlackBook:
    data = json.loads(Path("data/cocktails.json").read_text())

    return LittleBlackBook.model_validate(data)


def print_recipe(cocktail: Cocktail) -> str:
    recipe = ""
    recipe += f"You will be making a {cocktail.name}.\n"
    recipe += f"{cocktail.description}\n" if cocktail.description else ""

    for ingredient in cocktail.ingredients:
        name = (
            ingredient.nonLiquorType.name
            if not ingredient.isLiquor
            else f"{ingredient.liquorType.spirit} ({ingredient.liquorType.name})"
        )
        recipe += f"Add {ingredient.quantity} oz of {name}.\n"

    recipe += f"{cocktail.mixing} the ingredients.\n"
    recipe += (
        f"Serve {interpret_ice(cocktail.ice)}in a {cocktail.glass.lower()} glass.\n"
    )
    recipe += "Enjoy!"
    return recipe


def interpret_ice(ice: Ice) -> str:
    match ice:
        case ice.NONE:
            return ""
        case ice.ROCKS:
            return "on the rocks "
        case ice.CUBE:
            return "on a large cube of ice "
        case ice.PEBBLE:
            return "over pebble ice "
        case ice.CRUSHED:
            return "over crushed ice "

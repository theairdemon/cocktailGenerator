import json
from pathlib import Path

from pydantic import ValidationError

from models.cocktails import Cocktail, Ice, LittleBlackBook


def build_cocktail_book() -> LittleBlackBook:
    data = json.loads(Path("data/cocktails.json").read_text())

    return LittleBlackBook.model_validate(data)


def print_recipe(cocktail: Cocktail) -> str:
    recipe = ""
    recipe += f"You will be making a {cocktail.name}.\n"
    if cocktail.description:
        recipe += f"{cocktail.description}\n"

    for ingredient in cocktail.ingredients:
        if ingredient.isLiquor:
            if ingredient.liquorType.subtype:
                name = f"{ingredient.liquorType.subtype} {ingredient.liquorType.spirit}"
            else:
                name = f"{ingredient.liquorType.spirit}"

            if ingredient.liquorType.name:
                name += f" ({ingredient.liquorType.name})"

            recipe += f"Add {ingredient.quantity} oz of {name}.\n"
        else:
            units = ingredient.units.lower() if ingredient.units else "oz"
            recipe += f"Add {ingredient.quantity} {units} of {ingredient.nonLiquorType.name}.\n"

    recipe += f"{cocktail.mixing} the ingredients.\n"

    recipe += (
        f"Serve {interpret_ice(cocktail.ice)}in a {cocktail.glass.lower()} glass.\n"
    )
    if cocktail.garnish:
        recipe += interpret_garnish(cocktail.garnish.lower())
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


def interpret_garnish(garnish: str) -> str:
    return_string = "Garnish with a"
    if garnish[0] in ["a", "e", "i", "o", "u"]:
        return_string += "n"
    return_string += f" {garnish}.\n"
    return return_string

import random

from services.bar_storage import load_bar
from services.cocktail_builder import build_cocktail_book, print_recipe
from utils.utils import ask

cocktailBook = build_cocktail_book()
bar = load_bar()

barLiquorSpirits = {liquor.spirit for liquor in bar.liquors}
barNonLiquorNames = {nonLiquor.name for nonLiquor in bar.nonLiquors}

validCocktails = []


def cocktails_list(spiritType: str):
    validCocktails = []

    for cocktail in cocktailBook.allCocktails:
        if all(
            (
                (
                    (
                        ingredient.liquorType.spirit.lower() == spiritType.lower()
                        or not spiritType
                    )
                    and ingredient.liquorType.spirit in barLiquorSpirits
                )
                if ingredient.isLiquor
                else ingredient.nonLiquorType.name in barNonLiquorNames
            )
            for ingredient in cocktail.ingredients
        ):
            validCocktails.append(cocktail)

    return validCocktails


spiritType = ask("Enter preferred liquor (if any): ")
validCocktails = cocktails_list(spiritType)
tempValidCocktails = validCocktails.copy()

while True:
    if len(tempValidCocktails) == 0:
        tempValidCocktails = validCocktails.copy()

    randomCocktail = random.choice(tempValidCocktails)
    tempValidCocktails.remove(randomCocktail)
    recipe = print_recipe(randomCocktail)
    print(recipe)

    another = ask("Would you like another option? (y/n): ")
    if another.lower() == "n":
        break

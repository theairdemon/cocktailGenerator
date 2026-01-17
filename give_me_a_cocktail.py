import random

from services.bar_storage import load_bar
from services.cocktail_builder import build_cocktail_book, print_recipe

cocktailBook = build_cocktail_book()
bar = load_bar()

barLiquorSpirits = {liquor.spirit for liquor in bar.liquors}
barNonLiquorNames = {nonLiquor.name for nonLiquor in bar.nonLiquors}

validCocktails = []
for cocktail in cocktailBook.allCocktails:
    if all(
        (
            ingredient.liquorType.spirit in barLiquorSpirits
            if ingredient.isLiquor
            else ingredient.nonLiquorType.name in barNonLiquorNames
        )
        for ingredient in cocktail.ingredients
    ):
        validCocktails.append(cocktail)


randomCocktail = random.choice(validCocktails)
recipe = print_recipe(randomCocktail)
print(recipe)

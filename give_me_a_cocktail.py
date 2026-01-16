import random

from services.cocktail_builder import build_cocktail_book, print_recipe

cocktailBook = build_cocktail_book()

randomCocktail = random.choice(cocktailBook.allCocktails)

recipe = print_recipe(randomCocktail)

print(recipe)

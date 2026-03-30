# cocktailGenerator
A Python app for generating cocktails based off the contents of your bar.

# Overview

- `give_me_a_cocktail.py`: Generates a cocktail from your bar.
- `update_my_bar.py`: Update your bar with new liquors.
- `data/`
    - `bar.json`: Storage for the entire bar collection.
    - `cocktails.json`: Storage for all the cocktail recipes.
- `models/`
    - `bar.py`: Pydantic models for the bar itself - organizing liquors, etc.
    - `cocktails.py`: Pydantic models for various cocktail types/categories.
    - `liquors.py`: Pydantic models for various liquors in the bar.
- `services/`
    - `cocktail_builder.py`: Pulls in the cocktails from the stored JSON file and fits them into Pydantic models.
    - `bar_storage.py`: Writes-to the bar JSON and updates it with new or removed liquors.

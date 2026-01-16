import json
from pathlib import Path

from pydantic import ValidationError

from models.bar import Bar
from models.liquors import Liquor, NonLiquor


def stock_bar() -> Bar:
    data = json.loads(Path("data/bar.json").read_text())

    return Bar.model_validate(data)

    """
    liquors = []
    for item in data["liquors"]:
        liquors.append(Liquor.model_validate(item))

    nonLiquors = []
    for item in data["nonLiquors"]:
        nonLiquors.append(NonLiquor.model_validate(item))
    """

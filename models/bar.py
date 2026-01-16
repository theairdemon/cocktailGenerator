from pydantic import BaseModel

from models.liquors import Liquor, NonLiquor


class Bar(BaseModel):
    title: str
    bartender: str
    liquors: list[Liquor]
    nonLiquors: list[NonLiquor]

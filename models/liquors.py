from enum import Enum
from typing import Dict, Set, Union

from pydantic import BaseModel, field_validator


class Spirit(str, Enum):
    GIN = "Gin"
    WHISKEY = "Whiskey"
    VODKA = "Vodka"
    RUM = "Rum"
    TEQUILA = "Tequila"
    OTHER = "Other"


class GinSubtype(str, Enum):
    LONDON_DRY = "London Dry"
    OLD_TOM = "Old Tom"


class WhiskeySubtype(str, Enum):
    BOURBON = "Bourbon"
    RYE = "Rye"
    SCOTCH = "Scotch"


class VodkaSubtype(str, Enum):
    CLASSIC = "Classic"
    FLAVORED = "Flavored"


class RumSubtype(str, Enum):
    WHITE = "White"
    AGED = "Aged"
    SPICED = "Spiced"
    COCONUT = "Coconut"


class TequilaSubtype(str, Enum):
    BLANCO = "Blanco"
    REPOSADO = "Reposado"
    ANEJO = "Anejo"
    MEZCAL = "Mezcal"


Subtype = Union[GinSubtype, WhiskeySubtype, VodkaSubtype]

SUBTYPE_MATCHES: Dict[Spirit, Set[str]] = {
    Spirit.GIN: {s.value for s in GinSubtype},
    Spirit.WHISKEY: {s.value for s in WhiskeySubtype},
    Spirit.VODKA: {s.value for s in VodkaSubtype},
    Spirit.RUM: {s.value for s in RumSubtype},
    Spirit.TEQUILA: {s.value for s in TequilaSubtype},
}


class Liquor(BaseModel):
    name: str
    spirit: Spirit
    subtype: Subtype | str

    @field_validator("subtype")
    @classmethod
    def subtype_must_match_spirit(cls, v, info):
        spirit: Spirit | None = info.data.get("spirit")
        if spirit is None:
            return v

        # v might be an Enum instance; normalize to its string value
        value = v.value if isinstance(v, Enum) else str(v)

        if value not in SUBTYPE_MATCHES[spirit] and spirit != "OTHER":
            raise ValueError(
                f"subtype {value!r} not allowed for spirit {spirit.value!r}"
            )
        return v


class GenericNonLiquorType(str, Enum):
    SOUR = "Sour"
    SWEET = "Sweet"
    VERMOUTH = "Vermouth"
    WINE = "Wine"
    OTHER = "Other"


class NonLiquor(BaseModel):
    name: str
    type: GenericNonLiquorType


if __name__ == "__main__":
    # examples
    # Liquor(name="Maker's Mark", spirit="WHISKEY", subtype="Bourbon")  # ok
    # Liquor(name="Nope", spirit="WHISKEY", subtype="London Dry")  # error
    sample1 = {
        "name": "Maker's Mark",
        "spirit": "Whiskey",
        "subtype": "Bourbon",
    }
    liquor1 = Liquor.model_validate(sample1)
    print(liquor1.name, liquor1.spirit, liquor1.subtype)

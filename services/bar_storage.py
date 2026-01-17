import json
from pathlib import Path
from typing import Union

from models.bar import Bar
from models.liquors import Liquor, NonLiquor

BAR_PATH = Path("data/bar.json")


def load_bar(path: Path = BAR_PATH) -> Bar:
    if not path.exists():
        bar = Bar(liquors=[], nonLiquors=[])
        save_bar(bar, path)
        return bar

    data = json.loads(path.read_text(encoding="utf-8"))
    return Bar.model_validate(data)


def save_bar(bar: Bar, path: Path = BAR_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(bar.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    tmp.replace(path)


def add_item(bar: Bar, item: Union[Liquor, NonLiquor]) -> None:
    if isinstance(item, Liquor):
        bar.liquors.append(item)
    else:
        bar.nonLiquors.append(item)

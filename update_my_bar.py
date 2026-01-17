from pydantic import ValidationError

from models.liquors import Liquor, NonLiquor
from services.bar_storage import add_item, load_bar, save_bar


def ask(prompt: str) -> str:
    return input(prompt).strip()


def ask_yes_no(prompt: str) -> bool:
    while True:
        v = ask(prompt).lower()
        if v in {"y", "yes"}:
            return True
        if v in {"n", "no"}:
            return False
        print("Enter y/n.")


def create_liquor() -> Liquor:
    while True:
        payload = {
            "name": ask("Name: "),
            "spirit": ask("Spirit: "),
            "subtype": ask("Subtype: "),
        }
        try:
            return Liquor.model_validate(payload)
        except ValidationError as e:
            print(e)
            print("Try again.\n")


def create_nonliquor() -> NonLiquor:
    while True:
        payload = {
            "name": ask("Name: "),
            "type": ask("Type: "),
        }
        try:
            return NonLiquor.model_validate(payload)
        except ValidationError as e:
            print(e)
            print("Try again.\n")


def main() -> None:
    bar = load_bar()

    while True:
        is_liquor = ask_yes_no("Is it a liquor? (y/n): ")
        item = create_liquor() if is_liquor else create_nonliquor()
        add_item(bar, item)

        if not ask_yes_no("Add another? (y/n): "):
            break

    save_bar(bar)
    print("Saved.")


if __name__ == "__main__":
    main()

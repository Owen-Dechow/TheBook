from json import loads
import os
from typing import Callable, Any
from TheBook.settings import BASE_DIR

DIR = BASE_DIR / "base/data/pages"


class Recipe:
    name: str
    tags: list[str]
    creator: str
    ingredients: list[str]
    instructions: str
    id: int

    def __init__(self, data: dict, id: int):
        self.name = data["name"]
        self.tags = data["tags"]
        self.creator = data["creator"]
        self.ingredients = data["ingredients"]
        self.instructions = data["instructions"]
        self.id = id

    def __str__(self):
        if self.creator:
            return f"{self.name} ({self.creator})"
        else:
            return self.name

    @classmethod
    def get(cls, id: int):
        with open(DIR / f"page-{id}.json") as file:
            return cls(loads(file.read()), id)

    @classmethod
    def filter(cls, condition: Callable[[Any], bool]):
        out = []
        for path in os.listdir(DIR):
            if path.startswith("page-") and path.endswith(".json"):
                with open(DIR / path) as f:
                    r = Recipe(
                        loads(f.read()),
                        int(path.removeprefix("page-").removesuffix(".json")),
                    )
                    if condition(r):
                        out.append(r)

        return out

    @classmethod
    def all(cls):
        return cls.filter(lambda _: True)

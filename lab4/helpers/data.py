import json

__all__ = ["load_sample"]


def load_sample() -> None:
    with open("data/sample.json") as f:
        return json.load(f)

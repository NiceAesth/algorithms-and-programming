from __future__ import annotations

import json

__all__ = ["load_sample"]


def load_sample() -> list:
    with open("data/sample.json") as f:
        return json.load(f)

from __future__ import annotations

import datetime
import json

__all__ = ["load_sample"]


class DateTimeEncoder(json.JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


def load_sample() -> list:
    with open("data/sample.json") as f:
        return json.load(f)

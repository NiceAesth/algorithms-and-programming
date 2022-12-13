from __future__ import annotations

import datetime

import pytest
from helpers import data


def test_load_sample():
    """Test load_sample function."""
    assert data.load_sample() is not None


def test_json_encoder():
    """Test DateTimeEncoder class."""
    encoder = data.DateTimeEncoder()
    encoder.default(datetime.datetime.now()) is not None
    with pytest.raises(TypeError):
        encoder.default(None)

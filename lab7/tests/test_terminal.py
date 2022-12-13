from __future__ import annotations

from helpers import terminal


def post_increment(name, local={}):
    if name in local:
        local[name] += 1
        return local[name] - 1


def test_clear(monkeypatch):
    """Test clear function."""
    monkeypatch.setattr("os.system", lambda _: None)
    terminal.clear()


def test_read_int(monkeypatch):
    """Test read_int function."""
    index, data = 0, ["a", "1"]
    local = locals()
    monkeypatch.setattr(
        "builtins.input",
        lambda _: data[post_increment("index", local)],
    )
    terminal.read_int()


def test_read_student(monkeypatch):
    """Test read_student function."""
    monkeypatch.setattr("builtins.input", lambda _: "1")
    terminal.read_student()


def test_read_lab(monkeypatch):
    """Test read_lab function."""
    monkeypatch.setattr("builtins.input", lambda _: "1")
    terminal.read_lab()


def test_read_lab_problem(monkeypatch):
    """Test read_lab_problem function."""
    index, data = 0, [
        "a",
        "b",
        "c",
        "1_1",
        "name",
        "2021-01-01",
    ]
    local = locals()
    monkeypatch.setattr(
        "builtins.input",
        lambda _: data[post_increment("index", local)],
    )
    terminal.read_lab_problem()


def test_print_wait(monkeypatch):
    """Test print_wait function."""
    monkeypatch.setattr("builtins.input", lambda: "")
    terminal.print_wait()

import pytest

from app import add, greet


def test_greet():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_strips_whitespace():
    assert greet("  Bob  ") == "Hello, Bob!"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ")


def test_greet_rejects_non_string():
    with pytest.raises(TypeError):
        greet(123)


def test_add():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5

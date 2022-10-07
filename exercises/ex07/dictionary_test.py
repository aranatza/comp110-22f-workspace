"""Ex07 test file."""

__author__ = str("730560370")

import pytest
from dictionary import invert, favorite_color, count


def test_invert_01() -> None:
    """Use case of invert."""
    sample: dict[str, str] = {'apple': 'red', 'banana': 'yellow', 'lime': 'green'}
    assert invert(sample) == {'red': 'apple', 'yellow': 'banana', 'green': 'lime'}


def test_invert_02() -> None:
    """Use case of invert."""
    sample: dict[str, str] = {'110': 'comp'}
    assert invert(sample) == {'comp': '110'}


def test_invert_03() -> None:
    """Edge case of invert."""
    sample: dict[str, str] = {}
    assert invert(sample) == {}


def test_invert_error() -> None:
    """Optional test for key errors."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_colors_01() -> None:
    """Use case of favorite_colors."""
    sample: dict[str, str] = {"Allison": "yellow", "Emma": "red", "Anika": "red"}
    assert favorite_color(sample) == "red"


def test_favorite_colors_02() -> None:
    """Use case of favorite_colors."""
    sample: dict[str, str] = {"Allison": "red", "Emma": "blue", "Anika": "yellow"}
    assert favorite_color(sample) == "red"


def test_favorite_colors_03() -> None:
    """Edge case of favorite_colors."""
    sample: dict[str, str] = {}
    assert favorite_color(sample) == {}


def test_count_01() -> None:
    """Use case of count."""
    sample: list[str] = ["apple", "apple", "banana", "apple"]
    assert count(sample) == {'apple': 3, 'banana': 1}


def test_count_02() -> None:
    """Use case of count."""
    sample: list[str] = ["c", "a", "b", "b", "b", "c", "a", "c"]
    assert count(sample) == {'c': 3, 'a': 2, 'b': 3}


def test_count_03() -> None:
    """Edge case of count."""
    sample: list[str] = []
    assert count(sample) == {}
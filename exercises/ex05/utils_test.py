"""Exercise 5 - Utils testing file."""

__author__ = "730560370"


from utils import only_evens, sub, concat


def test_evens_01() -> None:
    """Use case of only_evens."""
    full_list: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(full_list) == [2, 4]


def test_evens_02() -> None:
    """Edge case of only_evens."""
    full_list: list[int] = []
    assert only_evens(full_list) == []


def test_evens_03() -> None:
    """Edge case of only_evens."""
    full_list: list[int] = [1, 3, 5]
    assert only_evens(full_list) == []


def test_concat_01() -> None:
    """Use case of concat."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6]


def test_concat_02() -> None:
    """Edge case of concat."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_03() -> None:
    """Edge case of concat."""
    list_1: list[int] = []
    list_2: list[int] = [44, 55, 66]
    assert concat(list_1, list_2) == [44, 55, 66]


def test_sub_01() -> None:
    """Use case of concat."""
    sub_list: list[int] = [1, 2, 3]
    assert sub(sub_list, 0, 3) == [1, 2, 3]


def test_sub_02() -> None:
    """Edge case of concat."""
    sub_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(sub_list, -5, 2) == [1, 2]


def test_sub_03() -> None:
    """Edge case of concat."""
    sub_list: list[int] = [1, 2, 3]
    assert sub(sub_list, 0, 7) == [1, 2, 3]
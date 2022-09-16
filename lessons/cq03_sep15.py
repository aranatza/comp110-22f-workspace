"""Example producing a function."""


def odds(min: int, max: int) -> list[int]:
    """Construct list of odds, inclusive."""
    xs: list[int] = list()
    i: int = (min // 2) * 2 + 1
    while i < max:
        xs.append(i)
        i += 2
    return xs


ys: list[int] = odds(3, 6)
print(ys)
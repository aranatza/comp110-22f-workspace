def odd_and_even(x: list[int]) -> list[int]:
    result: list[int] = []
    i: int = 0
    for item in x:
        if (i % 2) == 0:
            if (item % 2) != 0:
                result.append(item)
        i += 2
    return result
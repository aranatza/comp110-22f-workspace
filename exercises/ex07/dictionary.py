"""Ex07."""

__author__ = str("730560370")


def invert(original: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, the keys and values will be swapped."""
    inverted_dict: dict[str, str] = dict()
    for key in original:
        if original[key] in inverted_dict:
            raise KeyError("Sorry, key values cannot be duplicates!")
        inverted_dict[original[key]] = key
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Given a dictionary of names and favorite colors, the most popular color is returned."""
    tracker: dict[str, int] = dict()
    for key in colors:
        if colors[key] in tracker:
            tracker[colors[key]] += 1
        if colors[key] not in tracker:
            tracker[colors[key]] = 1
    if tracker == {}:
        return {}
    most_popular_int: int = 0
    most_popular_str: str = ""
    for key in tracker:
        if tracker[key] > most_popular_int:
            most_popular_int = tracker[key]
            most_popular_str = key
    return most_popular_str


def count(count_list: list[str]) -> dict[str, int]:
    """Given a list of strings, count will return a dict of unique keys and a count of how many times it appears."""
    final_dict: dict[str, int] = dict()
    for i in count_list:
        if i in final_dict:
            final_dict[i] += 1
        else:
            final_dict[i] = 1
    return final_dict
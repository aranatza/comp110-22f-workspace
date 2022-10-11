"""Exercise 5 - Utils (testing)."""

__author__ = "730560370"


def only_evens(full_list: list[int]) -> list[int]:
    """Given a list of numbers, returns those that are even."""
    i: int = 0
    even_list: list[int] = list()
    if len(full_list) == 0:
        return even_list
    while i == 0 or i < len(full_list):         # checks every index of the list including if the list is empty
        if full_list[i] % 2 == 0:
            even_list.append(full_list[i])
        i += 1
    return even_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two lists of ints, a new list will generate with the first list followed by the second list."""
    concat_list: list[int] = list()
    i: int = 0
    while i < len(list_1):
        concat_list.append(list_1[i])       # adds every index of one list to another
        i += 1
    i = 0
    while i < len(list_2):
        concat_list.append(list_2[i])       # adds every index of a list on top of the one that list_1 was added to
        i += 1
    return concat_list


def sub(sub_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates a list which is a subset of the given list, between the specified start and end index."""
    final_list: list[int] = list()
    if start_index < 0:
        start_index = 0                
    if end_index > len(sub_list):
        end_index = len(sub_list)        # 4 lines to ensure the integers are within the range of the list
    while start_index < end_index:
        final_list.append(sub_list[start_index])
        start_index += 1                 # Adds the value of every index within the given parameters
    return final_list
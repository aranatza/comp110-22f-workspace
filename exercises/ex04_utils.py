"""EX04 - List Utility Functions."""

__author__ = "730560370"


def all(all_list: list[int], all_int: int) -> bool:
    """Returns a true or false result when every number in a list is either equal, or not equal, to a following number."""
    if len(all_list) == 0:
        return False                                        # returns false (unequal) because the list is empty
    i: int = 0
    while i < len(all_list):
        if all_list[i] != all_int:
            return False                                    # returns False because at least one value is not equal to the given int
        i += 1
    return True                                             # returns true because every index of the list was found to equal the given number


def max(max_list: list[int]) -> int:
    """Searches a list for its maximum value."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")      # Error if the list is empty
    i: int = 0
    maximum_value: int = max_list[i]
    while i < len(max_list):                                # Compares every list index to another
        if i == 0 or max_list[i] > maximum_value:
            maximum_value = max_list[i]
        i += 1
    return maximum_value


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Determines if every value at every index in one list is equal to another."""
    if len(first_list) == 0 and len(second_list) == 0:      # A few lines to make sure the lists are of equal length and have values
        return True
    if len(first_list) != len(second_list):
        return False
    i: int = 0
    list_correctness: int = 0                               # A variable to keep track of how many indexes are equal to each other
    while i < len(first_list):
        if first_list[i] == second_list[i]:
            list_correctness += 1
        i += 1
    if list_correctness == len(first_list):
        return True
    return False
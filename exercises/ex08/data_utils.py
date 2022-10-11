"""Dictionary related utility functions."""

__author__ = "730560370"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a CSV file of data and represent it as a list of a dictionary."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)       
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(x: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first rows of data for each column."""
    result: dict[str, list[str]] = {}
    for keys in x:
        if n >= len(x[keys]):
            result = x
            return result
        tracker: list[str] = []
        i: int = 0
        while i < n:
            tracker.append(x[keys][i])
            i = i + 1
        result[keys] = tracker
    return result


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for columns in x:
        i: int = 0
        while i < len(y):
            if columns == y[i]:
                result[columns] = x[columns]
            i += 1
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two-column based tables combined."""
    result: dict[str, list[str]] = {}
    for columns in x:
        result[columns] = x[columns]
    for columns in y:
        if columns in result:
            result[columns] += y[columns]
        else:
            result[columns] = y[columns]
    return result


def count(x: list[str]) -> dict[str, int]:
    """Given a list, this function will produce a dictionary where each key is a unique value and the values are a count."""
    result: dict[str, int] = {}
    for i in x:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
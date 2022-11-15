"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730560370"


class Simpy:
    """Autograder Docstring."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Autograder Docstring."""
        self.values = values

    def __repr__(self) -> str:
        """Autograder Docstring."""
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        """Autograder Docstring."""
        self.values = []
        i: int = 0
        while i < y:
            self.values.append(x)
            i += 1
        return self.values
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Autograder Docstring."""
        self.values = []
        if start < stop:
            while start < stop:
                self.values.append(start)
                start += step
        if start > stop:
            while start > stop:
                self.values.append(start)
                start += step
        return None

    def sum(self) -> float:
        """Autograder Docstring."""
        return sum(self.values)
        
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Autograder Docstring."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for i in self.values:
                result.values.append(i + rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Autograder Docstring."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for i in self.values:
                result.values.append(i ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Autograder Docstring."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                if i == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Autograder Docstring."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                if i > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Autograder Docstring."""
        if isinstance(rhs, int):
            result: float
            for i in range(len(self.values)):
                if i == rhs:
                    result = self.values[i]
        else: 
            result: Simpy = Simpy([])
            for i in range(len(self.values)):
                if rhs[i] is True:
                    result.values.append(self.values[i])
        return result
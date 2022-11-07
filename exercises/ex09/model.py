"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt

# python -m mypy exercises/ex09


__author__ = "730560370"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Finds the distance between 2 points."""
        distance_between: float = sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))
        return distance_between
   

class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassign the object's location attribute."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Reassigns the object as infected (sick)."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns True/False if the cell is either vulnerable or infected."""
        return self.sickness == constants.VULNERABLE
    
    def is_infected(self) -> bool:
        """Returns whether or not the cell is infected."""
        return self.sickness >= constants.INFECTED

    def color(self) -> str:
        """Changes the color of a cell depending on it's sickness status."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "orange"
        elif self.is_immune():
            return "purple"

    def contact_with(self, other: Cell):
        """Infects vulnerable cells upon contact with infected cells."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        elif other.is_infected() and self.is_vulnerable():
            self.contract_disease()
    
    def immunize(self) -> None:
        """Assigns the Immunity constant to the sickness attribute to a cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns true if the sickness and immune constants are equal."""
        return self.sickness == constants.IMMUNE
    

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, num_infected_cells: int, num_immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if num_infected_cells <= 0 or num_infected_cells >= cells:
            raise ValueError("Some cells must be infected.")
        if num_immune_cells >= cells or num_immune_cells < 0:
            raise ValueError("Some cells must be immune.")
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < num_infected_cells:
                cell.contract_disease()
            elif i < num_infected_cells + num_immune_cells:
                cell.immunize()
            self.population.append(cell)
           
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed        
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0

        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0

        if cell.location.x <= constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0

        if cell.location.y <= constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for i in range(len(self.population)):
            if self.population[i].is_infected():
                return False
        return True

    def check_contacts(self) -> None:
        """Compares the distance between every 2 cell objects' locations."""
        for i in range(len(self.population)):
            for x in range(i + 1, len(self.population)):
                cell_1: Cell = self.population[i]
                cell_2: Cell = self.population[x]
                if cell_1.location.distance(cell_2.location) < constants.CELL_RADIUS:
                    cell_1.contact_with(cell_2)
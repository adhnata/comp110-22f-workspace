"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730616599"


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
    
    def distance(self, point_two: Point) -> float:
        """Find the distance between two points."""
        distance: float = sqrt(((point_two.x - self.x) ** 2) + ((point_two.y - self.y) ** 2))
        
        return distance
    

class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        
    def immunize(self) -> None:
        """Assign the immune constant to the sickness attribute for the cell the method was called on."""
        self.sickness = constants.IMMUNE
        
    def is_immune(self) -> bool:
        """Check to see if cell is sickness attribute is equal to immune constant."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
        
    def contract_disease(self) -> None:
        """Assign the infected constant to the sickness attribute for the cell the method was called on."""
        self.sickness = constants.INFECTED
        
    def is_vulnerable(self) -> bool:
        """Check if cell is immune or vulnerable to being infected."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
        
    def is_infected(self) -> bool:
        """Check to see if cell is already infected or not."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
        
    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Reassign object loaction attribute."""
        self.location = self.location.add(self.direction)
        
        if self.is_infected() is True:
            self.sickness += 1
        
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()
            
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        
        if self.is_infected() is True:
            return "red"
        
        if self.is_immune() is True:
            return "green"     
    
    def contact_with(self, second_cell: Cell):
        """If contact is made with two cells, infect the other if one cell is infected already."""
        if self.is_vulnerable() is True and second_cell.is_infected() is True:
            self.contract_disease()
                
        if self.is_infected() is True and second_cell.is_vulnerable() is True:
            second_cell.contract_disease()
   
class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0
    
    def __init__(self, cells: int, speed: float, infected: int, number_of_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        
        if infected >= cells or infected <= 0:
            raise ValueError("Some cells must start off infected, not all or none.")
            
        if number_of_immune > cells or number_of_immune < 0:
            raise ValueError("Some cells must start off immune, not all or none.")
        
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
            
        i: int = 0
        while i < infected:
            self.population[i].contract_disease()
            i += 1
    
    def check_contacts(self) -> None:
        """Check if any of the circles actually come into contact with each other."""
        i: int = 0
        while len(self.population) > i:
            y: int = i + 1
            while y < len(self.population):
                if self.population[i].location.distance(self.population[y].location) <= constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[y])
                    
                y += 1
                
            i += 1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        
        self.check_contacts()
        self.is_complete()

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
        
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
            
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
                 
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if (cell.is_infected()):
                return False
            return True
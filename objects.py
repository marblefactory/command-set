from abc import ABC
from enum import Enum

class Direction(Enum):
    """
    Represents the different the directions that the user can use.
    """
    LEFT      = 0
    RIGHT     = 1
    BACKWARDS = 2
    FORWARDS  = 3

    def __str__(self):
        """
        Defines the string representation of a Direction.
        """
        output = ["on the left", "on the right", "behind you", "straight ahead"]
        return output[self.value]



class MemoryIterationDirection(Enum):
    """
    Represents the direction of memory access in Rememebered objects.
        eg. The first door you went in  -> START_TO_END
        eg. The Last door you went in   -> END_TO_START
    """
    START_TO_END = 0
    END_TO_START = 1

    def __str__(self):
        """
        Defines the string representation of a StartPos.
        """
        output = ["START", "END"]
        return output[self.value]


class Location(ABC):
    """
    The abstract Location class.
    """
    pass


class Absolute(Location):
    """
    Represents an absolute location.
        eg. In the Building
    """
    pass

    def __str__(self):
        """
        Defines the string representation of an Absolute location.
        """
        return " in the building"


class Contextual(Location):
    """
    Represents a contextual location.
        eg. The 3rd door on your right.
    """
    direction: Direction # e.g. on the right
    num      : int       # e.g. 3rd (door)

    def __init__(self, direction: Direction = Direction.FORWARDS, num:int = 0):
        self.direction = direction
        self.num = num

    def __str__(self):
        """
        Defines the string representation Contextual location.
        """
        return str(self.num+1)+ "th " + str(self.direction)


class Rememebered(Location):
    """
    A location that has been visited before, and hense can be moved
    'back' to. Represented by an offset, and a starting end of an array,
    which are used to index the spy's memory.
    """
    offset: int
    iteration_dir: MemoryIterationDirection

    def __init__(self, iteration_dir:MemoryIterationDirection, offset:int = 0):
        self.offset = offset
        self.iteration_dir = iteration_dir

    def __str__(self):
        """
        Defines the string representation of a Rememebered Object.
        """
        return " the " + str(self.offset+1) + "th object from the " + str(self.iteration_dir) + " I remember."


class Object():
    """
    Represents a generic Object.
        eg. Table.
    """
    name    : str
    location: Location

    def __init__(self, name:str, location:Location=Contextual()):
        self.name     = name
        self.location = location

    def __str__(self):
        """
        Defines the string representation of an Object.
        """
        return self.name + " which is " + str(self.location)


class Relative(Object):
    """
    Represents a relative object.
        eg. Half way along the corridor.
    """
    to        : Object
    proportion: float

    def __init__(self, to:Object, proportion:float=1.0):
        self.to         = to
        self.proportion = proportion

    def __str__(self):
        """
        Defines the string representation of a Relative location.
        """
        if self.proportion > 0.8:
            amount = "the end of"
        elif 0.2 <= self.proportion <= 0.8:
            amount = "half way along"
        else:
            amount = "a bit along"

        return amount + " " + str(self.to)

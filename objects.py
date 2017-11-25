from abc import ABC
from enum import Enum
from locations import Location, Contextual
import numpy as np

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

    @classmethod
    def from_tensor_and_text(cls, tensor: np.ndarray, text:str):
        name     = "table"
        location = Location.from_tensor_and_text(tensor, text)
        return cls(name=name, location=location)



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

"""
TODO: Document
"""

from enum import Enum
from Actions import Action
from abc import ABC

class Speed(Enum):
    SLOW = 1
    MED  = 2
    FAST = 3


class Stance(Enum):
    PRONE  = 1
    CROUCH = 2
    STAND  = 3


class Direction(Enum):
    LEFT      = 1
    RIGHT     = 2
    BACKWARDS = 3
    FORWARDS  = 4


class Location(ABC):
    pass


class Absolute(Location):
    pass


class Contextual(Location):
    direction: Direction # e.g. on the right
    num: int             # e.g. 3rd (door)

    def __init__(self, direction: Direction = Direction.FORWARDS, num:int = 0):
        self.direction = direction
        self.num = num


class Object():
    name    : str
    location: Location

    def __init__(self, name:str, location:Location=Contextual()):
        self.name     = name
        self.location = location


class Relative(Object):
    to        : Object
    proportion: float

    def __init__(self, to:Object, proportion:float=1.0):
        self.to         = to
        self.proportion = proportion


class StartPos(Enum):
    START = 1
    END   = 2


class MemoryIndex():
    offset: int
    start: StartPos

    def __init__(self, start:StartPos, offset:int = 0):
        self.offset = offset
        self.start = start


class Rememebered(Object):
    obj: Object
    index: MemoryIndex

    def __init__(self, obj:Object, index:MemoryIndex):
        self.obj = obj
        self.index = index

class Move(Action):
    speed : Speed
    stance: Stance
    dest  : Object

    def __init__(self, to:Object, speed:Speed = Speed.MED, stance:Stance=Stance.STAND):
        self.speed  = speed
        self.stance = stance
        self.dest   = to

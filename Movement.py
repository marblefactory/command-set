"""
TODO: Document
"""

from enum import Enum
from Actions import Action
from abc import ABC

class Speed(Enum):
    SLOW = 0
    MED  = 1
    FAST = 2

    def __str__(self):
        output = ["SLOW", "MID", "FAST"]
        return output[self.value]



class Stance(Enum):
    PRONE  = 0
    CROUCH = 1
    STAND  = 2

    def __str__(self):
        output = ["PRONE", "CROUCH", "STAND"]
        return output[self.value]


class Direction(Enum):
    LEFT      = 0
    RIGHT     = 1
    BACKWARDS = 2
    FORWARDS  = 3

    def __str__(self):
        output = ["LEFT", "RIGHT", "BACKWARDS", "FORWARD"]
        return output[self.value]


class Location(ABC):
    pass


class Absolute(Location):
    pass

    def __str__(self):
        return ""


class Contextual(Location):
    direction: Direction # e.g. on the right
    num: int             # e.g. 3rd (door)

    def __init__(self, direction: Direction = Direction.FORWARDS, num:int = 0):
        self.direction = direction
        self.num = num

    def __str__(self):
        return "(" + str(self.num)+ "," + str(self.direction) + ")"


class Object():
    name    : str
    location: Location

    def __init__(self, name:str, location:Location=Contextual()):
        self.name     = name
        self.location = location

    def __str__(self):
        return "(" + self.name + ", " + str(self.location) + ")"


class Relative(Object):
    to        : Object
    proportion: float

    def __init__(self, to:Object, proportion:float=1.0):
        self.to         = to
        self.proportion = proportion

    def __str__(self):
        return "("+ str(self.to) + ", " + str(self.proportion) +")"

class StartPos(Enum):
    START = 0
    END   = 1

    def __str__(self):
        output = ["START", "END"]
        return output[self.value]


class MemoryIndex():
    offset: int
    start: StartPos

    def __init__(self, start:StartPos, offset:int = 0):
        self.offset = offset
        self.start = start

    def __str__(self):
        return "("+ str(self.start)+ ", "+ str(self.offset) +")"


class Rememebered(Object):
    obj: Object
    index: MemoryIndex

    def __init__(self, obj:Object, index:MemoryIndex):
        self.obj = obj
        self.index = index

    def __str__(self):
        return "(" + str(self.obj) + ", " + str(self.index) + ")"


class Move(Action):
    speed : Speed
    stance: Stance
    dest  : Object

    def __init__(self, to:Object, speed:Speed = Speed.MED, stance:Stance=Stance.STAND):
        self.speed  = speed
        self.stance = stance
        self.dest   = to

    def __str__ (self):
        return "(" + str(self.dest) + ", " + str(self.speed) +", " + str(self.stance) + ")"

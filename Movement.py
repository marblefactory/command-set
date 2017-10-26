"""
TODO: Document
"""

from enum import Enum
from Actions import Action


class Speed(Enum):
    SLOW = 1
    MED  = 2
    FAST = 3


class Stance(Enum):
    PRONE  = 1
    CROUCH = 2
    STAND  = 3


class Relation(Enum):
    SPECIFIC   = 1 # e.g. Room 256
    CONTEXTUAL = 2 # e.g. that room


class Object():
    name    : str
    relation: Relation

    def __init__(self, name:str, relation:Relation=Relation.CONTEXTUAL):
        self.name     = name
        self.relation = relation


class Relative(Object):
    to        : Object
    proportion: float

    def __init__(self, to:Object, proportion:float=1.0):
        self.to         = to
        self.proportion = proportion


class StartPos(Enum):
    START = 1
    END  = 2


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
    speed   : Speed
    stance  : Stance
    location: Object

    def __init__(self, location:Object, speed:Speed = Speed.MED, stance:Stance=Stance.STAND):
        self.speed    = speed
        self.stance   = stance
        self.location = location

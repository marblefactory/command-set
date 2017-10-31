from actions import Action
from objects import Object
from abc import ABC
from enum import Enum



class Speed(Enum):
    """
    Represents the differnt speeds that the user can specify.
    """
    SLOW = 0
    MED  = 1
    FAST = 2

    def __str__(self):
        """
        Defines the string representation of a Speed.
        """
        output = ["slowly", "", "quickly"]
        return output[self.value]


class Stance(Enum):
    """
    Represents the different stances that the user can specify.
    """
    PRONE  = 0
    CROUCH = 1
    STAND  = 2

    def __str__(self):
        """
        Defines the string representation of a Stance.
        """
        output = ["crawl", "crouch", "walk"]
        return output[self.value]


class Move(Action):
    """
    Represents a valid move.
    """
    speed : Speed
    stance: Stance
    dest  : Object

    def __init__(self, to:Object, speed:Speed = Speed.MED, stance:Stance=Stance.STAND):
        self.speed  = speed
        self.stance = stance
        self.dest   = to

    def __str__ (self):
        """
        Defines the string representation of a Move.
        """
        return str(self.speed) + " " + str(self.stance) + " to " + str(self.dest)

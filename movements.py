from actions  import Action
from objects  import Object
from abc      import ABC
from enum     import Enum
from networks import Movement_NN

import numpy as np


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
        output = ["slowly", "normally", "quickly"]
        return output[self.value]

    @classmethod
    def from_tensor(cls, tensor: np.ndarray):
        xs = [
            (Movement_NN.slow, Speed.SLOW),
            (Movement_NN.med,  Speed.MED),
            (Movement_NN.fast, Speed.FAST)
        ]

        return [speed for i, speed in xs if tensor[i]][0]


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

    @classmethod
    def from_tensor(cls, tensor: np.ndarray):
        xs = [
            (Movement_NN.prone, Stance.PRONE),
            (Movement_NN.crouch,  Stance.CROUCH),
            (Movement_NN.stand, Stance.STAND)
        ]

        return [stance for i, stance in xs if tensor[i]][0]


class Move(Action):
    """
    Represents a valid move.
    """
    speed  : Speed
    stance : Stance
    dest   : Object

    def __init__(self, to:Object, speed:Speed = Speed.MED, stance:Stance=Stance.STAND):
        self.speed  = speed
        self.stance = stance
        self.dest   = to

    def __str__ (self):
        """
        Defines the string representation of a Move.
        """
        return str(self.speed) + " " + str(self.stance) + " to " + str(self.dest)

    @classmethod
    def from_tensor_and_text(cls, tensor: np.ndarray, text: str):

        obj    = Object.from_tensor_and_text(tensor, text)
        stance = Stance.from_tensor(tensor)
        speed  = Speed.from_tensor(tensor)

        return  cls(to=obj, speed=speed, stance=stance)

from abc import ABC
from typing import Tuple



class Action(ABC):
    pass

class Composite(Action):
    actions:Tuple[Action]

    def __init__(self, *actions):
        self.actions = actions

    def __str__(self):

        return "("+ ". \n".join(map(str, self.actions)) +")"

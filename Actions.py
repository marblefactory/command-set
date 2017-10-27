from abc import ABC
from typing import Tuple



class Action(ABC):
    """
    An abstract class that all things that can be composed together must
    instanciate.

        eg. Move, Interact, etc.
    """
    pass

class Composite(Action):
    """
    An Action that is made by composing one or more Actions together in a
    sequential manner.
    """
    actions:Tuple[Action]

    def __init__(self, *actions):
        """
        Initalizes a composite action.

        Params:
            A variable number of actions.
        """
        self.actions = actions

    def __str__(self):
        """
        The string representation of an Action Composite.
        """
        return ",\nthen ".join(map(str, self.actions)) 

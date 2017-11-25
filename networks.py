
import numpy as np

class Movement_NN():
    slow   = 0
    med    = 1
    fast   = 2
    prone  = 3
    crouch = 4
    stand  = 5

    def run(self, input_tensor):
        """
        Returns a tensor:
        [ Slow   ]
        [ Med    ]
        [ Fast   ]
        [ Prone  ]
        [ Crouch ]
        [ Stand  ]
        """
        t = np.zeros(shape=(6,1), dtype=np.bool_)
        t[self.med]   = np.True_
        t[self.prone] = np.True_
        return t

class Location_NN():
    def run(self, input_tensor):
        return np.zeros(shape=(1,1), dtype=np.bool_)

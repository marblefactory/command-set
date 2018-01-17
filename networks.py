
import numpy as np
import text_processing

class Movement_NN():
    slow   = 0
    med    = 1
    fast   = 2
    prone  = 3
    crouch = 4
    stand  = 5

    def run(self, input_text):
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
    def run(self, input_text):
        """
        Returns a tensor:
        [ Absolute    ]
        [ Contextual  ]
        [ Directional ]
        """
        absolute = text_processing.d_absolute(input_text)
        contextual = text_processing.d_contextual(input_text)
        directional = text_processing.d_directional(input_text)

        tensor = np.array([absolute, contextual, directional])



        return np.zeros(shape=(1,1), dtype=np.bool_)

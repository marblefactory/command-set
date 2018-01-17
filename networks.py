
import numpy as np
from text_processing import *
from typing import List


def descriptor_vector(descriptors: List[Descriptor], text: str) -> np.array:
    """
    :return: a one-hot vector with a 1 at the position with the descriptor with the largest response on `text`.
             The vector is nx1, where n is the number of descriptors.
    """
    responses = [d.response(text) for d in descriptors]
    index = responses.index(max(responses))

    vec = np.zeros(shape=len(descriptors))
    vec[index] = 1

    return vec


class MovementNN():
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


class LocationNN():
    def absolute_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for absolute locations, e.g. Room 102
        """
        return DAnd([DWord('room'), DNumber()])

    def contextual_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for contextual locations, e.g. first door on the left
        """
        left_right = DXOR(DWord('left'), DWord('right'))
        return DAnd([DPositional(), DWordTag('NN'), left_right])

    def directional_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for directions, e.g. left, right, forwards, backwards
        """
        words = ['left', 'right', 'forwards', 'backwards']
        return DAnd.from_words(words)


    def run(self, input_text: str):
        """
        Returns a tensor:
        [ Absolute    ]
        [ Contextual  ]
        [ Directional ]
        """

        descriptors = [
            self.absolute_descriptor(),
            self.contextual_descriptor(),
            self.directional_descriptor()
        ]

        return descriptor_vector(descriptors, input_text)

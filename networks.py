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

    def slow_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for slow movement.
        """
        return WordMatch('slowly')

    def med_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for medium/normal movement
                 i.e. when there is no response for slow or fast.
        """
        return Not([self.slow_descriptor(), self.fast_descriptor()])

    def fast_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for fast movement.
        """
        return WordMatch('quickly')

    def prone_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for a prone stance.
        """
        return WordMatch('prone')

    def crouch_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for crouched stance.
        """
        return And([WordMatch('crouched'), WordMatch('crouching')])

    def stand_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for a standing stance.
                 i.e. when there is no response for prone or crouching.
        """
        return Not([self.prone_descriptor(), self.crouch_descriptor()])

    def run(self, input_text: str):
        """
        Returns a tensor:
        [ Slow   ]
        [ Med    ]
        [ Fast   ]
        [ Prone  ]
        [ Crouch ]
        [ Stand  ]
        """
        speed_descriptors = [
            self.slow_descriptor(),
            self.med_descriptor(),
            self.fast_descriptor()
        ]

        stance_descriptors = [
            self.prone_descriptor(),
            self.crouch_descriptor(),
            self.stand_descriptor()
        ]

        speed_vec = descriptor_vector(speed_descriptors, input_text)
        stance_vec = descriptor_vector(stance_descriptors, input_text)

        return np.append(speed_vec, stance_vec)


class LocationNN():
    def absolute_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for absolute locations, e.g. Room 102
        """
        return And([WordMatch('room'), Number()])

    def contextual_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for contextual locations, e.g. first door on the left
        """
        directions = ['left', 'right', 'behind', 'front']
        one_of = OneOf(WordMatch.list_from_words(directions))
        return And([Positional(), WordTag('NN'), one_of])

    def directional_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for directions, e.g. forwards, backwards
        """
        words = WordMatch.list_from_words(['forwards', 'backwards'])
        return And(words)

    def stairs_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for stairs, e.g. go upstairs
        """
        words = WordMatch.list_from_words(['upstairs', 'downstairs'])
        return And(words)

    def behind_obj_descriptor(self) -> Descriptor:
        """
        :return: a descriptor which produces a high response for going behind an object, e.g. go behind the sofas
        """
        return And([WordMatch('behind'), WordTag('NN')])


    def run(self, input_text: str):
        """
        Returns a tensor:
        [ Absolute    ] e.g. Go to room 201
        [ Contextual  ] e.g. Take the door behind you
        [ Directional ] e.g. Go forwards a little bit
        [ Stairs      ] e.g. Go downstairs
        [ Behind      ] e.g. Go behind the sofas
        """

        descriptors = [
            self.absolute_descriptor(),
            self.contextual_descriptor(),
            self.directional_descriptor(),
            self.stairs_descriptor(),
            self.behind_obj_descriptor()
        ]

        return descriptor_vector(descriptors, input_text)

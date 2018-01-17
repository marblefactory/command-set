import unittest
from text_processing import *


class MockDescriptor(Descriptor):
    """
    Returns the supplied response for every string.
    """
    def __init__(self, response: float):
        self.r = response

    def response(self, text: str) -> float:
        return self.r


class ThresholdDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests Threshold
    """
    def descriptor(self, value: float):
        return Threshold(MockDescriptor(value), 0.5)

    def test_below_threshold(self):
        assert self.descriptor(0.1).response(' ') == 0

    def test_on_threshold(self):
        assert self.descriptor(0.5).response(' ') == 1

    def test_above_threshold(self):
        assert self.descriptor(0.7).response(' ') == 1


class WordMatchDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests WordMatch
    """

    def descriptor(self):
        return WordMatch('hello')

    def test_no_response(self):
        assert self.descriptor().response('my sentence') == 0

    def test_single(self):
        assert self.descriptor().response('hello world') == 1

    def test_multiple(self):
        assert self.descriptor().response('hello world hello') == 2


class WordMeaningDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests WordMeaning
    """

    def descriptor(self):
        return WordMeaning('crouching')

    def test_single_small(self):
        assert self.descriptor().response('go') == 0.25

    def test_single_large(self):
        assert self.descriptor().response('crouching') == 1.0

    def test_multiple(self):
        assert self.descriptor().response('crouch crouching') == 2.0


class AndDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests And
    """

    def descriptor(self):
        words = WordMatch.list_from_words(['hello', 'world'])
        return And(words)

    def test_no_response(self):
        assert self.descriptor().response('my sentence') == 0

    def test_single(self):
        assert self.descriptor().response('hello sentence') == 0.5

    def test_single_rorder_invariant(self):
        assert self.descriptor().response('sentence hello') == 0.5

    def test_multiple(self):
        assert self.descriptor().response('hello world') == 1

    def test_multiple_order_invariant(self):
        assert self.descriptor().response('world hello') == 1

    def test_extra_word_invariant(self):
        assert self.descriptor().response('hello extra world extra') == 1


class PositionalDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests Positional
    """

    def descriptor(self):
        return Positional()

    def test_no_response(self):
        assert self.descriptor().response('take the door') == 0

    def test_single(self):
        assert self.descriptor().response('take the first door') == 1

    def test_multiple(self):
        assert self.descriptor().response('take the first second door') == 0


class WordTagDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests WordTag
    """

    def descriptor(self):
        """
        :return: a descriptor which matches on nouns.
        """
        return WordTag('NN')

    def test_no_response(self):
        assert self.descriptor().response('flying') == 0

    def test_single(self):
        assert self.descriptor().response('flying car') == 1

    def test_multiple(self):
        assert self.descriptor().response('flying car table') == 1


class NumberDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests Number
    """

    def descriptor(self):
        return Number()

    def test_no_response(self):
        assert self.descriptor().response('number') == 0

    def test_single(self):
        assert self.descriptor().response('105') == 1

    def test_multiple(self):
        assert self.descriptor().response('Room 802 and 700') == 2


class OneOfDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests OneOf
    """

    def descriptor(self):
        return OneOf([WordMatch('left'), WordMatch('right')])

    def test_no_response(self):
        assert self.descriptor().response('go forwards') == 0

    def test_single1(self):
        assert self.descriptor().response('go left') == 1

    def test_single2(self):
        assert self.descriptor().response('go right') == 1

    def test_multiple(self):
        assert self.descriptor().response('go left right') == 0


class NotDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests Not
    """

    def descriptor(self):
        return Not([WordMatch('hello'), WordMatch('world')])

    def test_no_response1(self):
        assert self.descriptor().response('hello') == 0

    def test_no_response2(self):
        assert self.descriptor().response('world') == 0

    def test_no_response3(self):
        assert self.descriptor().response('hello the world is blue') == 0

    def test_response(self):
        assert self.descriptor().response('no matched words in here') == 1

    def test_response_if_empty(self):
        assert self.descriptor().response('') == 1
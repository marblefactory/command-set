import unittest
from text_processing import *

class WordDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests DWord
    """

    def descriptor(self):
        return DWord('hello')

    def test_no_response(self):
        assert self.descriptor().response('my sentence') == 0

    def test_single(self):
        assert self.descriptor().response('hello world') == 1

    def test_multiple(self):
        assert self.descriptor().response('hello world hello') == 2


class AndDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests DAnd
    """

    def descriptor(self):
        return DAnd.from_words(['hello', 'world'])

    def test_no_response(self):
        assert self.descriptor().response('my sentence') == 0

    def test_single(self):
        assert self.descriptor().response('hello sentence') == 1

    def test_single_rorder_invariant(self):
        assert self.descriptor().response('sentence hello') == 1

    def test_multiple(self):
        assert self.descriptor().response('hello world') == 2

    def test_multiple_order_invariant(self):
        assert self.descriptor().response('world hello') == 2

    def test_extra_word_invariant(self):
        assert self.descriptor().response('hello extra world extra') == 2


class PositionalDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests DPositional
    """

    def descriptor(self):
        return DPositional()

    def test_no_response(self):
        assert self.descriptor().response('take the door') == 0

    def test_single(self):
        assert self.descriptor().response('take the first door') == 1

    def test_multiple(self):
        assert self.descriptor().response('take the first second door') == 1


class WordTagDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests DWordTag
    """

    def descriptor(self):
        """
        :return: a descriptor which matches on nouns.
        """
        return DWordTag('NN')

    def test_no_response(self):
        assert self.descriptor().response('flying') == 0

    def test_single(self):
        assert self.descriptor().response('flying car') == 1

    def test_multiple(self):
        assert self.descriptor().response('flying car table') == 2


class NumberDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests DNumber
    """

    def descriptor(self):
        return DNumber()

    def test_no_response(self):
        assert self.descriptor().response('number') == 0

    def test_single(self):
        assert self.descriptor().response('105') == 1

    def test_multiple(self):
        assert self.descriptor().response('Room 802 and 700') == 2


class XORDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests DXOR
    """

    def descriptor(self):
        return DXOR(DWord('left'), DWord('right'))

    def test_no_response(self):
        assert self.descriptor().response('go forwards') == 0

    def test_single1(self):
        assert self.descriptor().response('go left') == 1

    def test_single2(self):
        assert self.descriptor().response('go right') == 1

    def test_multiple(self):
        assert self.descriptor().response('go left right') == 0
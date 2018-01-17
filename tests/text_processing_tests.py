import unittest
from text_processing import *

class WordDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests the `d_word` function.
    """

    def test_no_response(self):
        assert d_word('hello')('my sentence') == 0

    def test_single(self):
        assert d_word('hello')('hello world') == 1

    def test_multiple(self):
        assert d_word('hello')('hello world hello') == 2


class AndDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests the `d_and` function.
    """

    def matcher(self):
        return d_and([d_word('hello'), d_word('world')])

    def test_no_response(self):
        assert self.matcher()('my sentence') == 0

    def test_single(self):
        assert self.matcher()('hello sentence') == 1

    def test_single_rorder_invariant(self):
        assert self.matcher()('sentence hello') == 1

    def test_multiple(self):
        assert self.matcher()('hello world') == 2

    def test_multiple_order_invariant(self):
        assert self.matcher()('world hello') == 2

    def test_extra_word_invariant(self):
        assert self.matcher()('hello extra world extra') == 2


class PositionalDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests the `d_positional` function.
    """

    def test_no_response(self):
        assert d_positional('take the door') == 0

    def test_single(self):
        assert d_positional('take the first door') == 1

    def test_multiple(self):
        assert d_positional('take the first second door') == 1


class NumberDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests the `d_number` function.
    """

    def test_no_response(self):
        assert d_number('number') == 0

    def test_single(self):
        assert d_number('105') == 1

    def test_multiple(self):
        assert d_number('Room 802 and 700') == 2


class XORDistanceMeasureTestCase(unittest.TestCase):
    """
    Tests the `d_xor` function.
    """

    def matcher(self):
        return d_xor(d_word('left'), d_word('right'))

    def test_no_response(self):
        assert self.matcher()('go forwards') == 0

    def test_single1(self):
        assert self.matcher()('go left') == 1

    def test_single2(self):
        assert self.matcher()('go right') == 1

    def test_multiple(self):
        assert self.matcher()('go left right') == 0
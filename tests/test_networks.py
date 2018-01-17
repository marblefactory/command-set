import unittest
from text_processing import Descriptor
from networks import descriptor_vector, LocationNN
import numpy as np



class MockDescriptor(Descriptor):
    """
    Returns the supplied response for every string.
    """
    def __init__(self, response: int):
        self.r = response

    def response(self, text: str) -> int:
        return self.r


class DescriptorVectorTestCase(unittest.TestCase):
    def test_descriptor_vector(self):
        d0 = MockDescriptor(0)
        d1 = MockDescriptor(1)
        d2 = MockDescriptor(2)

        vec = descriptor_vector([d0, d1, d2], 'some text')
        expected = np.array([0, 0, 1])

        assert np.array_equal(vec, expected)


class LocationNetworkTestCase(unittest.TestCase):
    def test_absolute(self):
        """
        Tests for a high response for an absolute location.
        """
        sentence = 'Go forwards to room 506'

        vec = LocationNN().run(sentence)
        expected = np.array([1, 0, 0])

        assert np.array_equal(vec, expected)

    def test_contextual_missing_position(self):
        """
        Tests for a high response for a contextual location even when missing the position (e.g. first, second, etc)
        """
        sentence = 'Take the door on your left'

        vec = LocationNN().run(sentence)
        expected = np.array([0, 1, 0])

        assert np.array_equal(vec, expected)

    def test_contextual(self):
        """
        Tests for a high response for a contextual location.
        """
        sentence = 'Take first door on your left'

        vec = LocationNN().run(sentence)
        expected = np.array([0, 1, 0])

        assert np.array_equal(vec, expected)

    def test_directional(self):
        """
        Tests for a high response for a directional location.
        """
        sentence = 'Go forwards'

        vec = LocationNN().run(sentence)
        expected = np.array([0, 0, 1])

        assert np.array_equal(vec, expected)
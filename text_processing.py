import nltk
from typing import Callable, List


def name_in(text: str):
    """
    :param text: the text the user spoke.
    :return: the name of the object the user is referring to.
    """
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    nouns = [(i, word) for i, (word, word_tag) in enumerate(tagged) if word_tag == 'NN']

    if nouns is None:
        raise Exception('No place name found')

    i, noun = nouns[0]

    # Find the name of the room.
    if noun == 'room' and i+1 < len(tokens):
        room_name = tokens[i+1]
        return 'room ' + room_name

    return noun


def nltk_tagged(tag: str, text: str) -> List[str]:
    """
    :return: a list of words with the NLTK tag `tag` in `text`.
    """
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    return [word for (word, word_tag) in tagged if word_tag == tag]


class Descriptor:
    """
    Produces a response when applied to a text.
    """

    def response(self, text: str) -> int:
        """
        :return: the response of the descriptor on the text.
        """
        pass


class DWord(Descriptor):
    """
    Matches on words in a text.
    """

    def __init__(self, word: str):
        """
        :param word: the word to be matched in the text.
        """
        self.word = word

    def response(self, text: str) -> int:
        """
        :return: the number of occurrences of `word` in the text.
        """
        matched_words = [w for w in text.split() if w == self.word]
        return len(matched_words)


class DAnd(Descriptor):
    """
    Matches on multiple conditions in a text.
    """

    def __init__(self, descriptors: List[Descriptor]):
        """
        :param descriptors: the descriptors for which the responses will be summed.
        """
        self.ds = descriptors

    def response(self, text: str) -> int:
        return sum([descriptor.response(text) for descriptor in self.ds])


class DPositional(Descriptor):
    """
    Matches on positional words, e.g. first, second, etc.
    """

    def response(self, text: str) -> int:
        """
        :return: 1 if any positional word is present in the text, or 0 if none are present.
        """
        nums = ['first', 'second', 'third', 'fourth']
        word_descriptors = [DWord(word) for word in nums]
        and_response = DAnd(word_descriptors).response(text)
        return int(and_response >= 1)


class DNumber(Descriptor):
    """
    Matches on numbers (e.g. 102) in a text.
    """

    def response(self, text: str) -> int:
        """
        :return: the number of numbers (e.g. 102) in the text.
        """
        numbers = nltk_tagged('CD', text)  # Tagged with Cardinal Number
        return len(numbers)


class DXOR(Descriptor):
    """
    Models an XOR gate, where if both descriptors match, there is a response of zero.
    """
    def __init__(self, d1: Descriptor, d2: Descriptor):
        self.d1 = d1
        self.d2 = d2

    def response(self, text: str) -> int:
        d1_resp = self.d1.response(text)
        d2_resp = self.d2.response(text)

        if (d1_resp == 0):
            return d2_resp
        elif (d2_resp == 0):
            return d1_resp
        return 0

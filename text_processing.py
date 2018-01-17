import nltk
from typing import List
from nltk.corpus import wordnet as wn


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
        raise NotImplementedError


class Word(Descriptor):
    """
    Matches based on individual words in a text.
    """
    word: str

    def __init__(self, word: str):
        """
        :param word: the word to be matched over the text.
        """
        self.word = word

    @classmethod
    def list_from_words(cls, words: List[str]) -> List['Word']:
        """
        :return: a list of word descriptors from the list of words.
        """
        return [cls(word) for word in words]


class WordMatch(Word):
    """
    Matches on words in a text.
    """

    def __init__(self, word: str):
        super(WordMatch, self).__init__(word)

    def response(self, text: str) -> float:
        """
        :return: the number of occurrences of `word` in the text.
        """
        matched_words = [w for w in text.split() if w == self.word]
        return len(matched_words)


class WordMeaning(Word):
    """
    Generates a response based on semantic similarity between words.
    """

    def __init__(self, word: str):
        super(WordMeaning, self).__init__(word)

    def response(self, text: str) -> float:
        def similarity(synset1, synset2) -> float:
            """
            :return: the maximum semantic similarity between the two synsets.
            """
            maximum = 0
            for s1 in synset1:
                for s2 in synset2:
                    sim = s1.path_similarity(s2) or 0
                    maximum = sim if sim > maximum else maximum

            return maximum

        word_synsets = wn.synsets(self.word)
        sentence_synsets = [wn.synsets(w) for w in text.split()]
        similarities = [similarity(word_synsets, synsets) for synsets in sentence_synsets]
        return sum(similarities)


class And(Descriptor):
    """
    Matches on multiple conditions in a text.
    """

    def __init__(self, descriptors: List[Descriptor]):
        """
        :param descriptors: the descriptors for which the responses will be summed.
        """
        self.ds = descriptors

    def response(self, text: str) -> float:
        return sum([descriptor.response(text) for descriptor in self.ds])


class Positional(Descriptor):
    """
    Matches on positional words, e.g. next, first, second, etc.
    """

    def response(self, text: str) -> float:
        """
        :return: 1 if any positional word is present in the text, or 0 if none are present.
        """
        positional_words = ['first', 'second', 'third', 'fourth', 'next']
        words = WordMatch.list_from_words(positional_words)
        and_response = And(words).response(text)
        return int(and_response >= 1)


class XOR(Descriptor):
    """
    Models an XOR gate, where if both descriptors match, there is a response of zero.
    """
    def __init__(self, d1: Descriptor, d2: Descriptor):
        self.d1 = d1
        self.d2 = d2

    def response(self, text: str) -> float:
        d1_resp = self.d1.response(text)
        d2_resp = self.d2.response(text)

        if d1_resp == 0:
            return d2_resp
        elif d2_resp == 0:
            return d1_resp
        return 0


class WordTag(Descriptor):
    """
    Matches on words with the given NLTK tag.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def response(self, text: str) -> float:
        """
        :return: the number of words matching the tag in the text.
        """
        return len(nltk_tagged(self.tag, text))


class Number(WordTag):
    """
    Matches on numbers (e.g. 102) in a text.
    """

    def __init__(self):
        super(Number, self).__init__('CD')  # Matches on Cardinal Numbers.


class Not(Descriptor):
    """
    Matches on the text if the other descriptors don't match, i.e. give a response of zero.
    """

    def __init__(self, descriptors: List[Descriptor]):
        self.ds = descriptors

    def response(self, text: str) -> float:
        """
        :return: 1 if **all** other descriptors give no a response, otherwise 0.
        """
        responses = [descriptor.response(text) for descriptor in self.ds]
        was_response = [r != 0 for r in responses]
        return int(not any(was_response))

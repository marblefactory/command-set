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


def d_word(word: str) -> Callable[[str], int]:
    """
    :return: the number of occurrences of `word` in the text.
    """
    def result(text: str):
        matched_words = [w for w in text.split() if w == word]
        return len(matched_words)

    return result


def d_and(functions: List[Callable[[str], int]]) -> Callable[[str], int]:
    """
    :return: the addition of the responses of the supplied functions on the text.
    """
    def result(text: str):
        return sum([func(text) for func in functions])

    return result


def d_positional(text: str) -> int:
    """
    :return: 1 if any positional words (e.g. 'first') occurs in the text, otherwise returns 0.
    """
    nums = ['first', 'second', 'third', 'fourth']
    words = [d_word(word) for word in nums]
    return int(d_and(words)(text) >= 1)


def d_number(text: str) -> int:
    """
    :return: the number of occurrences of numbers (e.g. '802') in the text.
    """
    numbers = nltk_tagged('CD', text) # Tagged with Cardinal Number
    return len(numbers)


def d_xor(f: Callable[[str], int], g: Callable[[str], int]) -> Callable[[str], int]:
    """
    Models an XOR gate.
    :return: 0 if both the functions give a positive response on the text. Or, returns the response of `f` on the text
             if `g` gives a response of 0, and vice versa.
    """
    def result(text: str):
        if (f(text) == 0):
            return g(text)
        elif (g(text) == 0):
            return f(text)
        return 0

    return result

import nltk
import inflect
from typing import Callable, List, Tuple



def nltk_tagged(tag: str, text: str) -> List[Tuple[int, str]]:
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    return [(i, word) for i, (word, word_tag) in enumerate(tagged) if word_tag == tag]


def name_in(text: str):
    """
    :param text: the text the user spoke.
    :return: the name of the object the user is referring to.
    """
    nouns = nltk_tagged('NN', text)

    if nouns is None:
        raise Exception('No place name found')

    i, noun = nouns[0]

    # Find the name of the room.
    if noun == 'room' and i+1 < len(tokens):
        room_name = tokens[i+1]
        return 'room ' + room_name

    return noun


# def d_word(word: str, text: str):
    # words_from_text = text.split()
    # return int(word in wwords_from_texts)
#
# def d_and(f: Callable , g: Callable ,text: str):
#     return d_word("left", text) + d_word("right", text)

def d_word(word: str) -> Callable[[str], int]:
    def result(text: str):
        return int(word in text.split())

    return result


def d_and(functions: List[Callable[[str], int]]) -> Callable[[str], int]:
    def result(text: str):
        return sum([func(text) for func in functions])

    return result


def d_positional(text: str) -> int:
    nums = ['first', 'second', 'third', 'fourth']
    words = [d_word(word) for word in nums]
    return d_and(words)(text)


def d_xor(f: Callable[[str], int], g: Callable[[str], int]) -> Callable[[str], int]:
    def result(text: str):
        if (f(text) == 0):
            return g(text)
        elif (g(text) == 0):
            return f(text)
        return 0

    return result




d_lefty_right = d_xor(d_word("left"), d_word("right"))

d_absolute    = d_word("room")
d_contextual  = d_and([d_lefty_right, d_positional])
d_directional = d_and([d_word("forwards"), d_word("backwards")])


sentence = "Go forwards"
# sentence = "Go to the first door on the right"
# sentence = "Go to room 802"

print(d_absolute(sentence))
print(d_contextual(sentence))
print(d_directional(sentence))

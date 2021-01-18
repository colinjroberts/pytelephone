import sys
import test
from PyDictionary import PyDictionary
import random
dictionary = PyDictionary()

words_to_ignore = ["a", "A", "an", "An", "this", "is", "was", "my", "your",
                   "This", "the", "The", "That", "that", "at", "At"]


def replace_a_word(l_o_w):
    # Replace one word in the sentence
    # if no synonyms, pick a different word
    list_of_replacement_words = None
    while list_of_replacement_words is None:
        num = random.randint(0, len(l_o_w)-1)
        word = l_o_w[num]
        if word not in words_to_ignore:
            stdout_ = sys.stdout  # Keep track of the previous value.
            list_of_replacement_words = dictionary.synonym(word)

            sys.stdout = stdout_  # restore the previous stdout.

    # print(list_of_replacement_words)
    replacement_num = random.randint(0, len(list_of_replacement_words)-1)
    l_o_w[num] = list_of_replacement_words[replacement_num]
    return l_o_w


def main():

    # Get number of alterations
    num_replacements_to_make = sys.argv[1]

    # Get input parse from a wav file
    initialText = test.main("mytest3.wav")[1:]
    initialText = initialText[:-1]

    # Split sentence into words
    list_of_words = initialText.split(" ")
    print(list_of_words)

    for times in range(int(num_replacements_to_make)):
        list_of_words = replace_a_word(list_of_words)
        print(list_of_words)

    return 0


main()

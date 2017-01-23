"""
CSCI-603: slippery_finger.py(Lab4)

This program is a spelling error correction system which
corrects user slippery finger errors and return the correct words.

__author__: Yu-ching Sun

"""

from mutable_str import mutable_str
import re

# word list set
word_list = set()

# dictionary for adjacent keys
letter_near = {}

def openfile(file):
    """
    Open words text file and put
    words in the set

    :param words text file
    :return: none
    """

    with open(file) as f:
        content = f.readlines()
        for line in content:
            words = line.strip()
            word_list.add(words)

def letter_near_func(file):
    """
    Open keyboard text file and put them in the dictionary,
    the first letter is the key and the rest are the values.

    :param file: keyboard text file
    :return: none
    """

    with open(file) as f:
        content = f.readlines()
        for line in content:
            words = line.strip()
            data = words.split(" ")

            # the letters after the first one
            sub = data[1:]

            # the first letter is the key,
            # the rest are the values
            letter_near[data[0]] = sub

def word_find( input ):
    """
    Find if the input is in the dictionary, or if the input is
    a slippery finger error and then corrects the input
    according to the dictionary.

    :param input: user input
    :return: mutable.__str__(): the string representation of the corrected word
    :return: input: the original user input
    """

    # if the input is in the word_list
    if input in word_list:
        return(input)

    else:

        # loop through each character in the word
        for i in range(len(input)):

            # if the letter is in the adjacent key dictionary
            if input[i] in letter_near.keys():

              # get the corresponding values
              adjacent_keys = letter_near[input[i]]
              mutable = mutable_str(input)
              for index in range(len(adjacent_keys)):

                 # replace each letter with the values in
                 # the adjacent key dictionary
                 mutable.__setitem__(i, adjacent_keys[index])

                 # if the altered word is in the dictionary
                 # (if it is correct) return it
                 if mutable.__str__() in word_list:
                    return mutable.__str__()

        return input

def main():
    """
    The main function

    :return: None
    """

    # punctuation marks string
    punc_string = ',;:.!? '

    # punctuation marks dictionary
    punc_dict = {}

    openfile("words.txt")
    letter_near_func("keyboard.txt")

    try:
        file = input("Enter file name: ")
        for line in open(file,'r').readlines():

            # the length of the user input
            user_input_size = len(line)

            # loop through the input
            for i in range(len(line)):

                # if the input has punctuation marks
                if line[i] in punc_string:

                    # put its index and puntuation mark in the dictionary
                    punc_dict[i] = line[i]

            # split the words when encountering space and punctuation marks
            different_words = re.split('\s|,|\.|!|\?|;|:',line)

            # correct string
            correct = ""

            # loop through line
            for i in different_words:

                # if i is a zero length space, skip it
                if i == '':
                    continue

                find_word_dict = word_find(i)

                # if the word is corrected in adjacent key case
                # append it to the correct string
                if find_word_dict in word_list:
                    correct = correct + find_word_dict

                    # get the index of the punctuation marks
                    punc_dict_keys = list(punc_dict.keys())

            # if there are punctuation marks in the input
            if len(punc_dict) > 0:

              # loop through the line
              for j in range (user_input_size):

                 for i in punc_dict.keys():

                   # if the index is originally the punctuation mark
                   # we insert the punctuation mark between corrected words
                   if j == i:
                      correct = correct[0:i] + punc_dict[i] + correct[i:]

            # clear the dictionary
            punc_dict.clear()

            print ("Output sentence: " + correct)

    except EOFError:
        pass

if __name__== "__main__":
    main()
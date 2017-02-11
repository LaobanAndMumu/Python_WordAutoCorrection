"""
CSCI-603: testSpeller.py(Lab4)

This program is a spelling error correction system which
corrects user slippery finger errors, missing a letter errors
and one misspelled character errors. Then the program returns the correct words.

__author__: Yu-ching Sun

"""
from mutable_str import mutable_str
import re

# word list set
word_list = set()

# dictionary for adjacent keys
letter_near = {}

def openfile(file):
    with open(file) as f:
        content = f.readlines()
        for line in content:
            words = line.strip()
            word_list.add(words)
            # print(words)

def compareTo(a,b):
    """
    Convert a and b
    to lower case and compare

    :param a: string
    :param b: set
    :return:
    """
    lowerA = a.lower()

    for x in b:
        if lowerA == str(x).lower():
            return str(x), True

    return a, False

def letter_near_func(file):
    """
    Create the dictionary for
    adjacent keys
    :param file:
    :return:
    """
    with open(file) as f:
        content = f.readlines()
        for line in content:
            words = line.strip()
            data = words.split(" ")
            # print(str(data[0:1]))
            sub = data[1:]
            letter_near[data[0]] = sub


def word_find( input ):
    """
    Replace each character with adjacent key's values

    :param input:
    :return:
    """

    if input in word_list:
        return(input)
    else:

        # loop through each character in the word
        for i in range( len(input) ):

            # get values for keys
            if input[i] in letter_near.keys():
              adjacent_keys = letter_near[input[i]]

              mutable = mutable_str(input)

              for index in range(len(adjacent_keys)):
                 mutable.__setitem__(i, adjacent_keys[index])

                 if mutable.__str__() in word_list:
                    return mutable.__str__()

        return input


def missing_one_letter( input ):
    """
    Insert a letter between characters
    :param input:
    :return:
    """

    add_input = ''

    # adjacent dictionary
    a_z = letter_near.keys()

    if input in word_list:
        return input
    else:
        for i in range(len(input)):
          for x in a_z:
            add_input = input[0:i] + x + input[i:]
            if add_input in word_list:
                return add_input
        return input

def replaceLetter(input):
    """
    Replace each letter with different letters
    until the matched word is found

    :param input:
    :return:
    """
    a_z = letter_near.keys()

    str1 = ''.join(a_z)

    mutable = mutable_str(input)

    for i in range(mutable.__len__()):
        mutable = mutable_str(input)
        for x in range(len(str1)):
            mutable.__setitem__(i,str1[x])

            if str(mutable) in word_list:
                return str(mutable)
    return('not found')


def main():
    """
    The main function

    :return: None
    """

    # dictionary
    openfile("words")

    # adjacent list dictionary
    letter_near_func("keyboard")

    user_input=''

    while user_input != 'exit':

        user_input = input('Enter a sentence or a word: ')

        userInputList = user_input.split()

        correct_output=''

        for i in userInputList:

            word, result = compareTo( str(i), word_list )

            if result == True:
                correct_output += ' ' + word
            else:

                notFound = word_find(word)

                word1, result1 = compareTo( notFound, word_list )

                if result1 == True:
                    correct_output += ' ' + word1
                else:
                    str2 = missing_one_letter(word1)
                    word2, result2 = compareTo( str2, word_list )

                    if result2 is True:
                        correct_output += ' ' + word2
                    else:
                        notfound2 = replaceLetter(word2)
                        word3, result3 = compareTo( notfound2, word_list )
                        if result3 is True:
                            correct_output += ' '+ word3
                        else:
                            correct_output += ' '+ word3

        print('Your input is:' + correct_output)

if __name__== "__main__":
    main()

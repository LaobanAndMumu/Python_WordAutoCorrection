"""
CSCI-603: spellfixer.py(Lab4)
This program is a spelling error correction system which
correct two types of input error, slippery finger and missing one letter.

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
    Find if the input is in the dictionary, or if the input is the
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
                 # (if it is corret) return it
                 if mutable.__str__() in word_list:
                    return mutable.__str__()

        return input

def missing_one_letter(input_one, user_input):
    """
    Find the correct word if the user misses one letter
    of a word.

    :param input_one: the user input
    :param user_input: create a space fo
    :return:
    """

    add_input = ""

    # create a list from a to z
    a_z = list(letter_near.keys())

    # if input is in the word lists
    if input_one in word_list:
        print(input_one)

    # if the input is not in the dictionary
    else:
        for i in range(len(input_one)):
          for x in a_z:

            # insert a to z before the first index to the last index
            add_input = input_one[0:i] + x + input_one[i:]

            # if the altered word is in the word list
            if add_input in word_list:

                # increment the index by one
                i += user_input.find(input_one)

                # return the index and corrected word
                return{i:add_input}

        return {0: input_one}

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

            # the length of the line
            user_input_size = len(line)

            # loop through the line
            for i in range(len(line)):

                # if the line has punctuation marks
                if line[i] in punc_string:

                    # put its index and puntuation mark in the dictionary
                    punc_dict[i] = line[i]

            # split the words when encountering space and punctuation marks
            different_words = re.split('\s|,|\.|!|\?|;|:',line)

            # correct string
            correct = ""

            # the return value for missing_one_letter function
            missing_correct = ""

            # loop through the line
            for i in different_words:

                # if i is a zero length space, skip it
                if i == '':
                    continue

                find_word_dict = word_find(i)

                # if the word is corrected in adjacent key case
                if find_word_dict in word_list:
                    correct = correct + find_word_dict

                # if the word is not corrected, call missing one letter function
                else:

                    missing_correct = list(missing_one_letter(i,line).values())[0]

                    # if the corrected word is in the dictionary
                    if missing_correct in word_list:

                        # the index of the letter
                        key_of_missing = list(missing_one_letter(i,line).keys())[0]

                        correct = correct + missing_correct

                        # get the index of the punctuation marks
                        punc_dict_keys = list(punc_dict.keys())

                        # if the index of the punctuation happens after the mispelled words
                        # increment the index of that punctuation by 1
                        for i in punc_dict_keys:
                            if i >= key_of_missing:
                                value = punc_dict[i]
                                del punc_dict[i]
                                key = i + 1
                                punc_dict[key] = value
                                user_input_size += 1
                    else:
                        correct = correct + missing_correct

            # if there are punctuation marks in the line
            if len(punc_dict) > 0:

              # loop through the line
              for j in range (user_input_size):

                 for i in punc_dict.keys():

                   # if the index is originally the punctuation mark
                   # we insert the punctuation mark between corrected words
                   if j == i:
                      correct = correct[0:i] + punc_dict[i] + correct[i:]

            print ("Output sentence: " + correct)

            # clear the dictionary
            punc_dict.clear()

    except EOFError:
        pass


if __name__== "__main__":
    main()

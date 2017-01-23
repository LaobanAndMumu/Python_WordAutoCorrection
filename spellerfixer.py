"""
CSCI-603: Spellfixer.py(Lab4)

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

def letter_near_func(file):

    with open(file) as f:
        content = f.readlines()
        for line in content:
            words = line.strip()
            data = words.split(" ")
            # print(str(data[0:1]))
            sub = data[1:]
            letter_near[data[0]] = sub


def word_find( input ):
    print("input " + input)

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
                #print(mutable, adjacent_keys[index])
                 if mutable.__str__() in word_list:
                    return mutable.__str__()
        return input


def missing_one_letter( input, user_input ):

    add_input = ""
    a_z =  list(letter_near.keys())
    print(a_z)
    if input in word_list:
        print(input)
    else:
        for i in range(len(input)):
          for x in a_z:
            add_input = input[0:i] + x + input[i:]
            if add_input in word_list:
                i += user_input.find(input)
                return{i:add_input}
        return {0:input}

def main():
    """
    The main function

    :return: None
    """

    punc_string = ",;:.! "
    punc_dict = {}
    openfile("words")

    letter_near_func("keyboard")
    user_input = input("Enter: ")
    user_input_size = len(user_input)

    for i in range(len(user_input)):
        if user_input[i] in punc_string:
            punc_dict[i] = user_input[i]
    print("Punction: " + str(list(punc_dict.values())))

    # split the words when encountering space and punctuation marks
    different_words = re.split('\s|,|\.|!|\?|;|:',user_input)

    print (different_words)

    correct = ""
    missing_correct = ""

    # loop through user input
    for i in different_words:

        # if i is a space, skip it
        if i == '':
            continue

        find_word_dict = word_find(i)

        # if the word is corrected in adjacent key case
        if find_word_dict in word_list:
            correct = correct + find_word_dict
            #print (correct)

        # if the word is not corrected, call missing one letter function
        else:

            missing_correct = list(missing_one_letter(i,user_input).values())[0]
            if missing_correct in word_list:
                key_of_missing = list(missing_one_letter(i,user_input).keys())[0]
                correct = correct + missing_correct
                #print (correct)
                punc_dict_keys = list(punc_dict.keys())
                for i in punc_dict_keys:
                    if i >= key_of_missing:
                        value = punc_dict[i]
                        del punc_dict[i]
                        key = i + 1
                        punc_dict[key] = value
                        user_input_size += 1
            else:
                correct = correct + missing_correct

    # if there are punctuations in the input
    if len(punc_dict) > 0:

      for j in range (user_input_size):
         for i in punc_dict.keys():
           if j is i:
              correct = correct[0:i] + punc_dict[i] + correct[i:]
              #print(correct)
    print (correct)

if __name__== "__main__":
    main()

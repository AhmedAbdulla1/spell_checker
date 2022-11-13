import difflib
from simple_colors import *
from time import time

dictionary = open("dictionary.txt", "r")  # open the dictionary file
dic_to_list = dictionary.read().split()  # set the dictionary in list


def binary_search(item, _list=dic_to_list):
    """
    search for the word in dictionary
    :param item
    :param _list
    :return: true or false
    """
    if len(_list) == 0:
        return False
    else:
        n = len(_list)
        mid = n // 2
        if _list[mid] == item:
            return True
        else:
            if item < _list[mid]:
                return binary_search(item, _list[:mid])
            else:
                return binary_search(item, _list[mid + 1:])

    # binary search with while lope
    # first, last = 0, len(_list) - 1
    # while first <= last:
    #     mid = (first + last) // 2

    #     if _list[mid] == item:
    #         return True
    #     elif item > _list[mid]:
    #         first = mid + 1
    #     else:
    #         last = mid - 1
    # return False


def sort(_max, index):
    """
    :param _max: list of value of SequenceMatcher
    :param index: list of words
    :return: none
    """
    for i in range(0, 4):
        if _max[i] > _max[i + 1]:
            _max[i], _max[i + 1] = _max[i + 1], _max[i]
            index[i], index[i + 1] = index[i + 1], index[i]


def get_suggestion(_word):
    """
    to get tree words suggestion for one wrong word
    :param _word:
    :return: list of suggestion words
    """
    index = [dic_to_list[0], dic_to_list[1], dic_to_list[2], dic_to_list[3], dic_to_list[4]]
    _max = [0, 0, 0,0,0]

    for item in dic_to_list:
        similar = difflib.SequenceMatcher(None, item, word).ratio()
        if similar >= 0.70 and similar > _max[0]:
            _max[0] = similar
            index[0] = item
            sort(_max, index)

    return index


class Format:
    end = '\033[0m'
    underline = '\033[4m'

    def print_wrong_word(self, _words, _wrongWords):
        """
        to print the wrong words and draw underline
        :param _words:
        :param _wrongWords:
        :return: None
        """
        for _word in _words:
            if _word in _wrongWords:
                print(red(Format.underline + _word + Format.end), end=' ')
            else:
                print(_word, end=' ')
        print()

    def print_suggestion(self, _wrongWords, _suggestionWords):
        """
        this function to print the suggestion words
        :param _wrongWords: this is the list of wrong words
        :param _suggestionWords: this is the dic of <wrongWords,list of suggestionWords>
        :return: None
        """
        for _word in _wrongWords:
            print(blue(_word) + ' : ' + ', '.join(_suggestionWords[_word]))


# start my program
content = input('enter your content:')
startTime = time()
wordlist = content.split()
wrongWords = []
for word in wordlist:
    if not binary_search(word):
        wrongWords.append(word)

suggestionWords = {}
for word in wrongWords:
    suggestionWords[word] = get_suggestion(word)
p = Format()
p.print_wrong_word(wordlist, wrongWords)
p.print_suggestion(wrongWords, suggestionWords)

print('time is : ' + str(time() - startTime))

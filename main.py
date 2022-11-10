import difflib
from simple_colors import *

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


def get_suggestions(_word):
    """
    search for the closest word
    :param _word:
    :return:
    """

    index = 0
    _max = 0

    for i in range(0, len(dic_to_list)):
        temp = difflib.SequenceMatcher(None, dic_to_list[i], _word)
        similar = temp.ratio()
        if similar > _max:
            _max = similar
            index = i
    return dic_to_list[index]


class Format:
    end = '\033[0m'
    underline = '\033[4m'


def formater(_words, _wrongWords):
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


def print_suggestion(_wrongWords, _suggestionWords):
    """
    this function to print the suggestion words
    :param _wrongWords: this is the list of wrong words
    :param _suggestionWords: this is the dic of <wrongWords,list of suggestionWords>
    :return: None
    """
    for _word in _wrongWords:
        print(blue(_word) + ' : ' + ' ,'.join(_suggestionWords[_word]))


# start my program
content = input('enter your content:')
wordlist = content.split()

wrongWords = []
for word in wordlist:
    if not binary_search(word):
        wrongWords.append(word)
suggestionWords = {
    'i': ['i'],
    'sofwear': ['soft', 'software'],
    'saem': ['sea', 'sae', 'same']

}
formater(wordlist, wrongWords)
print_suggestion(wrongWords, suggestionWords)

import sys
import random
from random import choice

def anagram(word_one, word_two):
    if word_one == word_two:
        return True
    else:
        return False

def create_dict_hash(words):
    dict = {}
    for i in range(len(words)):
        temp = sorted(words[i])
        new = " ".join(temp)
        dict[str(new)] = str(words[i])
    return dict
def get_anagrams(dict_of_words, word):
    result = list() #creates a list
    word1 = sorted(list(word)) # sorts list of words
    word1 = " ".join(word1)
    for key in dict_of_words.keys():
        if(key in word1):
            result.append(dict_of_words.get(key))
    return result

if __name__ == '__main__':
    #words = open("/usr/share/dict/words","r").read().split("\n")
    words = open("sherlock.txt", "r").read()
    word = choice(words)
    word1 = choice(words)
    dict_of_words = create_dict_hash(words)
    # print(dict_of_words)
    list_of_anagrams = get_anagrams(dict_of_words, word1)
    print(list_of_anagrams)
import random
from random import choice, randint
from sys import argv
import sys
from anagram import anagram
# takes an input
#num = int(input("please type a number: "))

# reusable opening and reading a file in python
# def get_file_lines(filename):
#     lines = []
#     file = open(filename, 'r')
#     clean_lines = [line.strip() for line in lines]
#     # for line in file:
#     #     lines.append(line.strip())
#     file.close()
#     return clean_lines
#     # or lines = file.readlines()
#    # return lines

# def get_set_words_from_file(path):
#     # Use a generator to put all lines into a set and return
#     return set(line.strip() for line in open('/usr/share/dict/words'))
#     # Use a generator to put all lines into a set and return
#     # opens a file of words 
#     # built in comput words file /usr/share/dict/words
#     #sherlock.txt
#     #code takes out the \n from the end of the words in the lists
#     #List comprehension of same code  


def read_words(words, number_of_words):
    # path = "/usr/share/dict/words"
    # words = get_set_words_from_file(path)
    words_list =[]
    for i in range(number_of_words):
        words_list.append(choice(words))
    return ''.join(words_list).capitalize() + ''
       

def create_dict_hash(words):
    dict = {}
    for i in range(len(words)):
        temp = sorted(words[i])
        new = "".join(temp)
        dict[str(new)] = str(words[i])
    return dict
     
'''def freq(str, num):
    
    # break string into a list of words
    str_list = str.split()
    
    #gives a set of new words
    unique_words = set(str_list)
    for words in unique_words:
        print(words, ' :', str_list.count(words))
'''

if __name__ == '__main__':
    words = list(open("/usr/share/dict/words","r"))
    dict = create_dict_hash(words)
    print(read_words(words, int(sys.argv[1])))
    word1 = random.choice(words)
    # word1 = word1[:len(word1)-2]
    word2 = random.choice(words)
    # word2 = word2[:len(word2)-2]
    # if(sorted(word1) in dict):
    #     print("1111")
    while(anagram(word1, word2) == False):
         word1 = random.choice(words)
         word1 = word1[:len(word1)-2]
         word2 = random.choice(words)
         word2 = word2[:len(word2)-2]

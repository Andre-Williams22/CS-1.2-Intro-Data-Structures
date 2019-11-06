import sys
import re

def get_word(file_name='sherlock.txt'):
    # opens and closes comments
    file = open(file_name, 'r')
    read_words = file.readlines()
    file.close()

    text = list()
    # gets rid of extra space and characters after the words on each line
    for line in read_words:
        split_line = line.strip().split(" ")
        for word in split_line:
            if (word.lower != ""):
                text.append(word.lower().strip("(),!."""))

    return text

    #Another way to open and read text from a file 
    
    # words = list(open("sherlock.txt","r"))
    # text = re.sub(r'[^a-zA-Z\s]', '', words)
    # text = text.split()
    
    # for line in words:
    #     split_line = line.strip().split(" ")
    #     for word in split_line:
    #         text.remove(word)
    #         text.append(word.lower().strip("(),!.""")) 

def tuples_hist(words):
    word_list = []
    for word in words:
        word_found = False
        for tup in word_list:
            #checks to see if item in wordlist is a tuple
            if tup[0] == word:
                count = tup[1]
                word_list.remove(tup)
                #adds words to a dictionary as a tuple 
                word_list.append((word, count + 1))
                word_found = True
        if word_found != True:
            word_list.append((word, 1))

    return word_list


if __name__ == '__main__':
    
    print(tuples_hist(get_word()))

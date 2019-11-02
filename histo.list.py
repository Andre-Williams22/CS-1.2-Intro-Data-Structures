import sys
import re

def get_word(file_name='sherlock.txt'):
    file = open(file_name, 'r')
    read_words = file.readlines()
    file.close()

    text = list()

    for line in read_words:
        split_line = line.strip().split(" ")
        for word in split_line:
            if (word.lower != ""):
                text.append(word.lower().strip("(),!."""))

    return text
    # words = list(open("sherlock.txt","r"))
    # text = re.sub(r'[^a-zA-Z\s]', '', words)
    # text = text.split()
    
    # for line in words:
    #     split_line = line.strip().split(" ")
    #     for word in split_line:
    #         text.remove(word)
    #         text.append(word.lower().strip("(),!.""")) 

def list_hist(words):
    word_list = []
    for word in words:
        word_found = False
        for item in word_list:
            if item[0] == word:
                item[1] += 1
                word_found = True

        if not word_found:
            word_list.append([word, 1])
    return word_list


if __name__ == '__main__':
    
    print(list_hist(get_word()))

# creates a sentence function that walks through the histogram 

import random

def random_num_words(content):
    """A function that returns a list of words and returns a random list of words. """
    words_list = []

    num_of_words = random.randrange(2, len(content)) #grabs number of words from the words file
    # print(f"Random number of words: {num_of_words}") # Check output
    for wordindex in range(num_of_words):
        word = content[wordindex]
        # print(f'the word: {word} ') #check output 
        words_list.append(word)
    return words_list


def put_in_sentence(gets_words_list):
    # clean_list = []
    sentence = ''
    words_list = gets_words_list
    for word_index in range(len(words_list)):
        word = words_list[word_index]
        sentence += " " + word

    return sentence 
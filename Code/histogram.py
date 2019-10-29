import sys
import re

def new_histogram(words):
    '''return a new histogram'''
    histogram = {}
    for word in words:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram

def unique_words(histogram):
    '''returns unique words in histogram'''
    total = len(histogram)
    return total

def frequency(histogram, word):
    '''returns frequency of a word'''
    if word in histogram:
        return histogram[word]
    else:
        return False

if __name__ == '__main__':
    
    with open("sherlock.txt",'r') as file:
        text = file.read()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = text.split()
    
    for word in text:
        text.remove(word)
        text.append(word.lower())

    dict = new_histogram(text)
    print(dict)

    print(unique_words(new_histogram(text)))
    print(frequency(new_histogram(text), sys.argv[1]))
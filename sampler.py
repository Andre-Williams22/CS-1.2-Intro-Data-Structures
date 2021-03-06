from itertools import product
import random 
import histogram
import sys
import re
from utils import time_it
# one fish two fish red fish blue fish

def sample_by_frequency(histogram):
    """return a word from this histogram, randomly sampled by weigthinhg each word's probability
    of being chosen by its observed frequency. """
    # tokens = sum([count for word, count in histogram]) #count total tokens
    # dart = random.randint(1, tokens) # throws a dart on number line
    # fence = 0
    # for word, count in histogram: #loops over each word and its counts
    #     fence += count #add the count to the fence which moves fence to the right of number line
    #     if fence >= dart: #checks if words fence is past dart
    #         return  word #fence is past the dart so choose this word


    rand_val = random.random()
    total = 0
    percent_range = 0
    
    # for k,v in histogram.items():
    #     total += v
    # Faster than code above for grabbing values in keys   
    for value in histogram.values():
        total += value
    
    for key in histogram.keys():
        # finds the probability of each event in dictionary 
        percent_range += (histogram[key] / total)
        # checks to see if random value is in range of that event
        if rand_val <= percent_range:
            #returns the word instead of value
            return key
@time_it
def test_sample_by_frequency(hist):
    """ Runs a test function for the words in the histogram"""
    results = []
    #runs the iteration a thousand 
    for _ in range(1000):
        results.append(sample_by_frequency(hist))
    test_hist = histogram.new_histogram(results)
    for keys in test_hist.keys():
        print(f"{keys} {test_hist[keys]} ")


def non_uniform_sample(histogram): # creates a non-uniform sample function 
    """ Generate a random word based on non-uniform distribution"""
    words_frequency = 0 # create words_frequency 
    for key, value in histogram.items(): # loop through histogram 
        words_frequency += value # append words to words_frequency 
    random_num = random.randint(0, words_frequency-1) # generate random number 
    count = 0 # create count var 
    for word, freq in histogram.items(): # loop through hist.items
        count += freq # increment count by frequency 
        if random_num < count: # check if random_num is less than count 
            return word # return word







if __name__ == "__main__":
    #word_counts = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
    #print(sample_by_frequency(word_counts))
    with open(sys.argv[1],'r') as file:
        text = file.read()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = text.split()

    # for word in text:
    #     text.remove(word)
    #     text.append(word.lower())

    # call fish.txt in argument
    test_sample_by_frequency(histogram.new_histogram(text))
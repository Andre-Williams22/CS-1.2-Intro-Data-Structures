from itertools import product
import random 
import histogram
import sys
import re
from utils import time_it
# one fish two fish red fish blue fish

def sample_by_frequency(histogram):
    """select a word based on frequency"""
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
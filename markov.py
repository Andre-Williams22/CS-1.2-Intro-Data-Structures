# from dictogram import Dictogram
# import random
# import sys


# def markov_model(word_list):
#     markov = dict()
#     for i in range(len(word_list)-1):
#         current_word = word_list[i]
#         next_word = word_list[i+1]


# class Markogram(dict):
#     def __init__(self, words):
#         """Initialize this histogram as a new dict and count given words."""
#         super().__init__()
#         # Add properties to track useful word counts for this histogram
#         self.types = 0  # Count of distinct word types in this histogram
#         self.tokens = 0 # Total count of all word tokens in this histogram
#         # Count words in given list, if any

#         for i in range(len(words)):
#             word = words[i]


#             try:
#                 following_word = words[i+1]
#             except:
#                 break

#         dictogram_word = self.get(word, None)

#         if dictogram_word is not None:
#             dictogram_word.add_count(following_word, 1)

#         else:
#                 self[words] = Dictogram([following_word]) # creates a new dictogram for the word

        

#     # def add_count(self, word):
#     #     """adds word to markogram"""
#     #     if not word in self.keys():
#     #         self[word] = Dictogram()
#     #         self.types += 1
#     #     else: 
#     #         self[word][1] += 1 
#     #     self.tokens += 1

#     def sample(self, key):
#         """gets a random word  that appears after key"""
#         total = self.tokens
#         sum_prob = 0
#         prediction = random.random()
#         for key in self.keys():
#             prob = self[key][1]/total
#             if prediction > sum_prob and prediction <= sum_prob + prob:
#                 return key 
#             sum_prob += prob

#     def get_string(self, length=10):
#         """returns a string of len based on markov's chain"""
#         start = random.choice(list(self.keys()))
#         strings = [start]
        
#         for _ in range(length-1):
#             next_word = self.sample(start)[0]
#             strings.append(next_word)
#         return strings

#     def new_sentence(self, count=10):
#         words = self.get_string(count)
#         return ' '.join(words).capitalize() + '.'


# def iframe(tag):
#     ''' takes in the str and adds iframe tag and takes it into a link'''
#     print(f'IFRAME TAG: {tag}')
#     tag = tag.split(' ')
#     print(tag)
#     gifs = []
#     for index in range(len(tag)):
#         print(f'EACH WORD: {tag[index]}')
#         if "https://" in tag[index]:
#             print('HELLOOOOOOOOOOOOO')
#             print(f"URL{tag[index]}")
#             gifs.append(tag[index])

#     return " ".join(tag), gifs
from dictogram import Dictogram 
from pprint import pprint
import random
import re
from sampler import *

text = "one fish two blue fish fish red fish blue red fish END"
# text = 'how much wood would a wood chuck chuck if a wood chuck could chuck wood END'
texts_list = text.split()

def make_markov_model(words_list):
    """Generates histogram"""
    markov_model = dict() # create a dictionary
    for i in range (0, len(words_list)-1): # loop through the words
        current_word = words_list[i]
        next_word = words_list[i+1]
        if current_word in markov_model:
            # We have to just append to the existing histogram
            markov_model[current_word].add_count(next_word)
        else:
            markov_model[current_word] = Dictogram([next_word])
    return markov_model

def generate_random_start(model):
    # To just generate any starting word uncomment line:
    # return random.choice(model.keys())

    # To generate a "valid" starting word use:
    # Valid starting words are words that started a sentence in the corpus
    print('MODEL: {}'.format(model))
    for k, v in model.items():
        for inner_key, inner_value in v.items():
            if inner_key == 'END':
                seed_word = 'END'
                while seed_word == 'END':
                    seed_word = sample_by_frequency(v)
                return seed_word

def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    print(f"corrent_word")
    print("****** Cur word: {}".format(current_word))
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_model[current_word]
        print("****** Cur dictogram: {}".format(current_dictogram))
        random_weighted_word = sample_by_frequency(current_dictogram)
        if random_weighted_word == 'END':
            break
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'


model = make_markov_model(texts_list)

print(model)





# if __name__ == "__main__":
    
        
#     words = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda! https://google.com"
#     #dic = Markogram(words.split())
#     # for key in dic.keys():
#     #     print(f"{key}: {dic[key]}")
#     # print(dic.sample('a'))
#     # print(f"tokens: {dic.tokens}")
#     # print(f"types: {dic.types}")
#     #print(dic.get_string(10))
#     print(dic)
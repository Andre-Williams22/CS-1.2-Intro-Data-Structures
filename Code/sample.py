from itertools import product
import random 
text = "one fish two fish red fish blue fish"

word_counts = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

def sample_by_frequency(histogram):
    # select a word based on frequency
    rand_val = random.random()
    total = 0
    
    for k,v in histogram.items():
        total += v
        if rand_val <= total:
            return k
    assert False, 'unreachable'
print(sample_by_frequency(word_counts))

# def probability(dice_number, sides, target):
#     rollAmount = sides**dice_number
#     targetAmount = 0
#     for i in map(sum, product(range(1,sides+1), repeat=dice_number)):
#         if i == target:
#             targetAmount += 1
#     odds = targetAmount / rollAmount
#     return odds

# print(probability(1, 6, 5))


# def get_random_word():

from collections import Counter, defaultdict
from utils import time_it

# @time_it
# def anagram(words):
#     anagrams = defaultdict(list)
#     for word in words:
#         histogram = tuple(Counter(word).items()) # builds a hastable histogram
#         anagrams[histogram].append(word)
#     return list(anagrams.values())


@time_it
def findanagranfromlistofwords(li):
    dict = {}
    index=0
    for _ in range(0,len(li)):
        originalfirst = li[index]
        sortedfirst = ''.join(sorted(str(li[index])))
        for j in range(index+1,len(li)):
            next = ''.join(sorted(str(li[j])))
            #print(next)
            if sortedfirst == next:
                dict.update({originalfirst:li[j]})
                print("dict = ",dict)
        index+=1

    print(dict)

if __name__ == "__main__":

    findanagranfromlistofwords(["car", "tree", "boy", "girl", "arc", "yob"])    
   
   
   
    # keywords = ("hi", "hello", "bye", "helol", "abc", "cab", 
#                 "bac", "silenced", "licensed", "declines")

# print(anagram(keywords))
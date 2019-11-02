import random
import sys
# a = input('please type a word: ')
# b = input('please type a word: ')
# c = input('please type a word: ')
# d = input('please type a word: ')
# e = input('please type a word: ')

# words = []

# words.append(a)
# words.append(b)
# words.append(c)
# words.append(d)
# words.append(e)


# print ("The list before shuffling is : ", end="")
# for i in range(0, len(words)):
#     print(words[i], end=" ")
# print("\r")


# random.shuffle(words)
# print(random.choice(words))

# # Printing list after shuffling 
# print ("The list after shuffling is : ", end="") 
# for i in range(0, len(words)): 
#     print (words[i], end=" ") 
# print("\r") 




def rearrange(words):
    result = [] 
    for i in range(len(words)):
        word = random.choice(words)
        result.append(word)
        words.remove(word)
    result = result [:-1]
    return(result)
    


def reverse(words):
    new_list = words[::-1]
    print(new_list)

if __name__ == '__main__':
    words = list(sys.argv[1:])
    temp = rearrange(words)
    print(temp)
    print(reverse(temp))
import random

# f = open('/usr/share/dict/words', 'r')

# words = f.readlines()
# f.close()
num = int(input("please type a number: "))


# def function(words, num):
#         for word in range(0, len(words)):
#             word = random.choice(words) 
#             #words[0].split(' ')
#             #num = random.choice(words)
#             return word


def read_words(num):
    words_list =[]
    with open('/usr/share/dict/words') as f: 
        words = f.readlines()
        for i in range(int(num)):
            word = random.choice(words)
            words_list.append(word)
            #code takes out the \n from the words in the lists
        words_list = [word.rstrip() for word in words_list]
        return(" ".join(words_list))

   
     


print(read_words(num))

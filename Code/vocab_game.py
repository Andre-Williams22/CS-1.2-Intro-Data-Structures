
# Let's play a vocabulary game where user's guess the word and definition
import random

answer = input("Would you like to play: y or n ")
print(" ")
while answer == 'y':
        
    hashtable = {'bonjour': 'hello', 'enchante': 'nice to meet you', 'jemapple': 'my name is', 'je': 'I', 'See you later': 'A plus tard'}


    keywordlist = list(hashtable.keys()) # turns words into a list
    random.shuffle(keywordlist)
    correct = 0
    wrong = 0


    for word in keywordlist:
        show = "{}"
        print(show.format(word))
        userinput = input("Answer: ")
        print(hashtable[word])
        print(" ")


        if userinput == hashtable[word]:
            print("CORRECT")
            correct += 1
        else:
            print("wrong")
            wrong += 1
            
            print('_'*25)

    display = "SCORE: {} correct and {} wrong"
    print(display.format(correct, wrong))

    answer = input("Play again? ")
print(" ")
print("Thanks for playing")


# def secret_word(words):
#     for k,v in hashtable.items():
#         random_word = random.choice(k)
        
#     return guessed_word(random_word)

# def guessed_word(random_word, guessed_definition)




# if __name__ == '__main__':
#     print(secret_word(hashtable))
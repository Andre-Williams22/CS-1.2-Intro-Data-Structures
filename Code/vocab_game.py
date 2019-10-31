
# Let's play a vocabulary game where user's guess the word and definition
import random

#answer = input("Would you like to play a french vocabulary game? y or n: ")
print(" ")
print("_"*50)
print("Welcome to the game.")
print("Let's test your french vocabulary!")
while True:
        
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
        display = "SCORE: {} correct and {} wrong"
        print(display.format(correct, wrong))
        print('_'*25)

    if wrong >= 3:
        if input("play again: ") in "Yy":
            wrong = 0
            correct = 0 
        else:
            break

print(" ")
print("Thanks for playing")


# def secret_word(words):
#     for k,v in hashtable.items():
#         random_word = random.choice(k)
        
#     return guessed_word(random_word)

# def guessed_word(random_word, guessed_definition)




# if __name__ == '__main__':
#     print(secret_word(hashtable))
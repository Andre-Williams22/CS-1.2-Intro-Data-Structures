import random

a = input('please type a word ')
b = input('please type a word ')
c = input('please type a word ')
d = input('please type a word ')
e = input('please type a word ')

words = []

words.append(a)
words.append(b)
words.append(c)
words.append(d)
words.append(e)

print(random.choice(words))


print ("The list before shuffling is : ", end="")
for i in range(0, len(words)):
    print(words[i], end=" ")
print("\r")

random.shuffle(words)


# Printing list after shuffling 
print ("The list after shuffling is : ", end="") 
for i in range(0, len(words)): 
    print (words[i], end=" ") 
print("\r") 
string = " it was the best of times it was the worst of times. it was the age of wisdom it was the age of foolishness"
wordlist = string.split()

#wordfreq = []

#for item in wordlist:
    #wordfreq.append(wordlist.count(item))
wordfreq = [wordlist.count(item) for item in wordlist] #list comprehension 


print("pairs: " + str(list(zip(wordfreq, wordlist))))
#print("pairs: " + str(list(zip([wordfreq, [wordlist]]))))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

'''
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux
'''
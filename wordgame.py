import random
from copy import copy
''' Word game '''
with open('/usr/share/dict/words','r') as w:
    words = w.read().splitlines()

numWords = 10 
allWords = [words[i] for i in random.sample(range(len(words)),numWords)]

hiddenWord = allWords[0]
displayWords = allWords[1:]

print displayWords

choice = str((raw_input ('Ready? [y]es\n')))
choice = choice.strip()
if choice == 'y':
    indexToRemove = random.randint(0,len(displayWords))
    
    displayWordsNew = copy(displayWords)
    random.shuffle(displayWordsNew)
    displayWordsNew[indexToRemove] = hiddenWord
    
    print displayWordsNew
    word = str(raw_input ('Which is the different word\n'))
    if word == displayWordsNew[indexToRemove]:
        print "You got it right"
        print displayWords
        print displayWordsNew
    else:
        print "Oops, you got it wrong, but it's a difficult game! The correct word was"
        print displayWordsNew[indexToRemove]
        
else:
    exit()

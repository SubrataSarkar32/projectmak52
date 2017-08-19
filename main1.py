import checkword1
o=5
def mainwork(letter,word,word2,wordl):#checks for letter in word
         global o
         if letter in word:
            displaytext = letter + ' is in the word.'
            word3,wordl=checkword1.chekword1(letter,word,word2,wordl)            
         else:
            displaytext = letter + ' is not in the word.'
            word3,wordl=checkword1.chekword1(letter,word,word2,wordl)
            o-=1            
         return displaytext,o,word3,wordl
def reset():#resets o to 0
    global o
    o=5

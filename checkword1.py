def chekword1(letter,word,word2,wordl):#checks for letter in word
    
    for i in range(len(word)):
        if word[i]==letter:
            wordl[i]=letter
    word2=''
    for i in range(len(word)):
        word2+=wordl[i]    
    return word2,wordl


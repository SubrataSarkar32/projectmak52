ForL1=[]
Lst2=[]
def insForL1(letter):#checks for letter in list
    global ForL1
    if letter not in ForL1:
        ForL1+=[letter]
    return ForL1
def insLst2(letter):#checks for letter in list of non-forbidden letter
    global Lst2
    if letter not in Lst2:
         Lst2+=[letter]
    return Lst2
def reset():#resets all variables
    global ForL1
    ForL1=[]
    global Lst2
    Lst2=[]

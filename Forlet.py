def Forbidlet():
    print 'DOES IT CONTAIN FORBIDDEN LETTER'
    import random
    import increase
    import checkchar
    alLst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
     'S','T','U','V','W','X','Y','Z']
    alLst1=alLst
    ForLst=[]
    for i in range(4):
        a=random.randint(0,len(alLst)-1)
        ForLst+=alLst1.pop(a)
    
    chance=0    
    ForL1=[]
    Lst2=[]
    print 'guess an word,input"*" any time to quit'
    k=True
    while k==True:
        c=0
        letter1=raw_input('Enter a your guess:')
        letter1=letter1.upper()
        if letter1=='*':
            k=False
            break
            
        if len(letter1)>1:
           chance=increase.increase()
           for q in range(len(letter1)):
               letter=letter1[q]
               
               if letter in ForLst:
                                 
                   ForL1=checkchar.insForL1(letter)              
                   if len(ForL1)<=4:
                       
                       print ForLst                  
                       if len(ForL1)==4:
                           print 'You have taken',chance,'atttempts'
                           print 'Sorry you lost... \n GAME OVER!!! The letters were',ForLst
                           increase.reset()
                           checkchar.reset()
                           break
                       else:
                          g=raw_input( "Do you want to continue? There is a Forbidden Letter.Press y to continue or n to quit:")
                          g=g.capitalize()
                          if g== 'N':                       
                              print 'You have taken',chance,'atttempts'
                              print "You loose","Sorry you lost... \n GAME OVER!!! The letters were",ForLst
                              increase.reset()
                              checkchar.reset()
                              k=False
                              break
                          elif g=='Y':
                              break
               elif letter in alLst:
                  c+=1
                  
                  Lst2=checkchar.insLst2(letter)
                  
                  if c==len(letter1):
                      print 'You have taken',chance,'atttempts'
                      print"You win","Hurray! You win The forbidden letters were",ForLst
                      increase.reset()
                      checkchar.reset()
                      k=False
                      break
           
               else:
                   print 'You did enter an non-alphabet'
           print 'The non-forbidden letters you guessed are',Lst2
           print 'The forbidden letters you guessed are ',ForL1
        
        else:
           print "Do not Enter a single character only."

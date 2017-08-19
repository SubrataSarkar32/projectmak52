def Highlow():
    print '============================================================'
    print 'HIGH OR LOW'
    import random
    import increase
    number=random.randint(1,50)    
    chance=0
    print 'Press * any time to quit.Guess a number between 1 to 50'
    k=True
    while k==True:
        E1=input('Enter a your guess:')
        if E1>number:
            print 'Your guess is higher than original number.'
            chance=increase.increase()
        elif E1<number:
            print 'Your guess is lower than original number.'
            chance=increase.increase()
        elif E1==number:
            print "You win","Hurray!!! You guessed it in",chance,"turns.The number was ",number," \
  CONGRATS! YOU WIN!"
            break
        elif E1=='*':
            k=False
            break
        else:
            print 'Enter a number'
        while chance%5==0:
            h=raw_input('Press y to continue else n to quit')
            h=h.capitalize()
            if h=="Y":
                break
            elif h=="N":
                "You loose","Sorry you lost... \n GAME OVER!!! The number was",number
                k=False
                chance+=1
    print'You took',chance-1,'attempts'
    increase.reset()
    print '============================================================='

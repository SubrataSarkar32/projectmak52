def uniplay():
    print "This game has been made by PA Game SSDDR.\
    Enter game number to play the game or credit to see description of game\
    maker.Press n to exit."
    n=True
    while n!=False:
        print " 1. Hangman \n 2. Cow and bull \n 3. High or low \n 4. Does it haveforbidden letter? \n 5. Credit\n 6. CC Lisence"
        n=raw_input('Enter your choice:')
        n=n.capitalize()
        if n=="1":
            import hangman
            hangman.Hangman()
        elif n=="2":
            import cowandbull1
            cowandbull1.Cowbull()
        elif n=="3":
            import Highlow
            Highlow.Highlow()
        elif n=="4":
            import Forlet
            Forlet.Forbidlet()
        elif n=="5":
            import members
            members.credit()
        elif n=="6":
            import cc
            cc.license1()
        elif n=="N":
            n=False
        else:
            print "Invalid input"
uniplay()        


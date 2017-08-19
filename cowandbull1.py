def Cowbull():
 import random
 print '=============================================================='
 print "Welcome to the game of"
 print "    COWS AND BULLS    "
 number = random.randint(1000,9999) 
 attempts = 0
 ni2=True
 while ni2==True:
     guess = raw_input("\nGuess a 4 digit number: ")
     if guess=='*':
             ni2=False
             break
     elif guess.isdigit():
             guess=int(guess)
             guess_str = str(guess)
             num = str(number)
             length = len(guess_str)
             if length != 4:
                 print "You did not enter a 4 digit number."
                 ni2=True
                 
             else:    
                if guess == number:
                   print "\nHURRAY!!! \nYou guessed it in {} turns. The number was {} ".format(attempts,number)
                   print "                  !!!CONGRATS YOU WON!!!                    "
                   ni2=False
                cows = bulls = 0
                for i in range (length):
                    if guess_str[i] == num[i]:
                        bulls += 1
                    elif guess_str[i] in num:
                        cows += 1
                print "{} Cows and {} Bulls".format(cows,bulls)
                if cows == 4:
                   print "\nSorry you lost... \nGAME OVER!!!"
                   ni2=False
                               
     else:
             print 'Enter number only'
             
     
 print 'You took',attempts,'attempts'   
 print "\nThanks for playing."
 print '==================================================================='

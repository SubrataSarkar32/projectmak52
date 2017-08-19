try:
    import pickle
    file0 = open('sl.dat','rb')
    file1 = open('log.dat','rb')
    file1.close()
    file0.close()
    file9 = open('log.dat','rb')
    try :
           while True :
                y = pickle.load(file9)
                y = str(int(y,2))
                if y=='1':
                    pass
                elif y=='9635' or y=='5369':
                    file9.close()
                    
                    raise ValueError
                    break
                else:
                    file9.close()
                    
                    raise EnvironmentError
                    
    except EOFError:
                   pass
    file9.close()
    x=''
    print 'THIS IS A PRODUCT OF PA Games SSDDR.\n By clicking on I Agree you comply with Creative Commons Lisence\n Games by PA Games is licensed under the \nCreative Commons Attribution-NonCommercial 4.0 International License.\n To view a copy of this license,\n visit http://creativecommons.org/licenses/by/4.0/ or \n send a letter to Creative Commons, PO Box 1866, \n Mountain View, CA 94042, USA.\nYou may use parts of this program with consent to the makers for free.\n\
    The members of PA Games SSDDR include: \n 1.Subrata Sarkar(<subrotosarkar32@gmail.com>) \n \
    2.Dibyendu Das(<dibyendudgp10@gmail.com>) \n 3.Souhardya Sen(<souhardya147@gmail.com>) \n 4.Rajdeep Deogharia(<deogharia.17@gmail.com>) \n \
    5.Debabrata Mukherjee(<debmuk.dm@gmail.com>) \n WEBSITE: pagamesltd.blogspot.com'
    uio=True
    while uio==True:
        d=raw_input('Enter product code: ')
        file9 = open('log.dat','rb')
        try :
           uio=True
           while uio==True :
                y = pickle.load(file9)
                y = str(int(y,2))
                if y=='1':
                    pass
                elif y=='9635' or y=='5369':
                    file9.close()
                    uio=False
                    raise ValueError
                    break
                else:
                    file9.close()                    
                    raise EnvironmentError
                    print "Product Mishandled",'Contact PA Games SSDDR with a screenshot of this window. \n\
You have changed some game files'
                    break
        except EOFError :
                   pass
        except KeyError:
            print "Product Mishandled",'Contact PA Games SSDDR with a screenshot of this window. \n\
You have changed some game files'
            break
        file9.close()
        file0 = open('sl.dat','rb')
        try :            
            x=[]
            while True :
                y = pickle.load(file0)
                x+=[y]
            
        except EOFError :
                pass
        file0.close()
        
        
        a=str(int(x[0],2))
        b=str(int(x[1],2))
        
        if d==a:
           file1 = open('log.dat','wb')
           x1 = bin(int(a))
           pickle.dump(x1,file1)
           file1.close()
           uio=False
           print "Product Activated", "Thank You for using our program.\n The Professional version of the game has been activated."
           import uniplay
        elif d==b:
           file1 = open('log.dat','wb')
           x1 = bin(int(b))
           pickle.dump(x1,file1)
           file1.close()
           uio=False
           print "Product Activated", "Thank You for using our program.\n The General User version of the game has been activated."
           import uniplay

except IOError:
        print 'some .dat files are missing'
except ValueError:
    import uniplay
except EnvironmentError:
    
    print "Product Mishandled",'Contact PA Games SSDDR with a screenshot of this window. \n\
You have changed some game files'
    

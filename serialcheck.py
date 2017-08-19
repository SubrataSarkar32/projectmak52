try:
    import pickle
    file0 = open('sl.dat','rb')
    file1 = open('log.dat','rb')
    file1.close()
    file0.close()
    
    import Tkinter
    import os.path
    def load_image(file):# function to load images
        '''This function returns original image if PIL is present else runs not avaible image'''
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file1 = os.path.join(main_dir, 'data', file)
        q=Tkinter.PhotoImage(file=file1)
        return q
    import tkMessageBox
    root=Tkinter.Tk()
    root.title('Product Registration')
    file9 = open('log.dat','rb')
    try :
           while True :
                y = pickle.load(file9)
                y = str(int(y,2))
                if y=='1':
                    pass
                elif y=='9635' or y=='5369':
                    file9.close()
                    root.destroy()
                    raise ValueError
                    break
                else:
                    file9.close()
                    
                    raise EnvironmentError
                    
    except EOFError:
                   pass
    file9.close()
    root.minsize('355','400')
    x=''
    L0 = Tkinter.Label(root,bg="#FF9940",fg="white", text="THIS IS A PRODUCT OF PA Games Ltd.\n By clicking on I Agree you comply with Creative Commons Lisence\n Games by PA Games is licensed under the \nCreative Commons Attribution-NonCommercial 4.0 International License.\n To view a copy of this license,\n visit http://creativecommons.org/licenses/by/4.0/ or \n send a letter to Creative Commons, PO Box 1866, \n Mountain View, CA 94042, USA.\nYou may use parts of this program with consent to the makers for free.\n\
    The members of PA Games Ltd. include: \n 1.Subrata Sarkar(<subrotosarkar32@gmail.com>) \n \
    2.Dibyendu Das(<dibyendudgp10@gmail.com>) \n 3.Souhardya Sen(<souhardya147@gmail.com>) \n 4.Rajdeep Deogharia(<deogharia.17@gmail.com>) \n \
    5.Debabrata Mukherjee(<debmuk.dm@gmail.com>)")
    L0.place(x='0',y='0')
    E1 = Tkinter.Entry(root, bd =5)
    E1.place(x='110',y='230')
    noimg=load_image('88x31.GIF')
    label=Tkinter.Label(root,image=noimg)
    label.place(x='120',y='260')
    noimg1=load_image('ccpagames1.GIF')
    labelp=Tkinter.Label(root,image=noimg1)
    labelp.place(x='0',y='232')
    def quitee():
        d=E1.get()
        file9 = open('log.dat','rb')
        try :
           while True :
                y = pickle.load(file9)
                y = str(int(y,2))
                if y=='1':
                    pass
                elif y=='9635' or y=='5369':
                    file9.close()
                    root.destroy()
                    raise ValueError
                    break
                else:
                    file9.close()
                    
                    raise EnvironmentError
                    tkMessageBox.showinfo( "Product Mishandled",'Contact PA Games Ltd. with a screenshot of this window. \n\
You have changed some game files')
        except EOFError :
                   pass
        file9.close()
        file0 = open('sl.dat','rb')
        try :            
            x=[]
            while True :
                y = pickle.load(file0)
                x+=[y]
            return x
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
           tkMessageBox.showinfo( "Product Activated", "Thank You for using our program.\n The Professional version of the game has been activated.")
           root.destroy()
           import try32
        elif d==b:
           file1 = open('log.dat','wb')
           x1 = bin(int(b))
           pickle.dump(x1,file1)
           file1.close()    
           tkMessageBox.showinfo( "Product Activated", "Thank You for using our program.\n The General User version of the game has been activated.")
           root.destroy()
           import try32
    
    C = Tkinter.Button(root, text ="I Agree",relief="groove",bg="#109070",fg="white", command = quitee,font=("arial",18,"bold"))
    C.place(x='50',y='330')
    id1 = Tkinter.Button(root, text ="I Disagree",relief="groove",bg="#FF3050",fg="white", command =root.destroy ,font=("arial",18,"bold"))
    id1.place(x='200',y='330')
    root.mainloop()
except IOError:
        print 'some .dat files are missing'
except ValueError:
    import try32
except EnvironmentError:
    
    tkMessageBox.showinfo( "Product Mishandled",'Contact PA Games Ltd. with a screenshot of this window. \n\
You have changed some game files')
    root.destroy()


import Tkinter
import random,os.path
def load_image(file):# function to load images
        '''This function returns original image if PIL is present else runs not avaible image'''
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, 'data', file)        
        try:
             from PIL import ImageTk,Image
             q = ImageTk.PhotoImage(Image.open(file))
             return q
        except ImportError:
             print 'PIL not found.Please install and run'
             q=Tkinter.PhotoImage(file=str((os.path.join(main_dir, 'data','nopagames.GIF'))))
             return q
             
game=Tkinter.Tk()#Here the main parent program strats
game.title("PA Games SSDDR")

game.maxsize(488, 508)
game.minsize(488, 508)

img0 = load_image('pagames.GIF')
img9 = load_image('pagames1.JPG')
img = load_image('mann1.JPG')
img10 = load_image('members4.JPG')
L6 = Tkinter.Label(game, image = img0)
L6.pack(side = Tkinter.TOP,fill = Tkinter.BOTH)

def run2(event=None):#opens members credits window
    import Tkinter
    
    import tkMessageBox
    game.mem = Tkinter.Toplevel()
    
    game.mem.title("Members")
    game.mem.minsize(600, 600)
    game.mem.transient(game)
    img3 = load_image('members4.JPG')
    L = Tkinter.Label(game.mem, image = img3)
    L.pack(side =Tkinter.TOP,fill = Tkinter.BOTH, )
    def destroy(event=None):
            game.mem.destroy()
    game.mem.bind('<Escape>',destroy)
    game.mem.mainloop()

def run(event=None):#opens intermidiate window
    import Tkinter
    
    import tkMessageBox
    game.start = Tkinter.Toplevel()
    
    game.start.title("Hangman")
    game.start.minsize(600, 600)
    game.start.transient(game)

    var8 = Tkinter.StringVar()
    var8.set("The Computer selects a Random Word.Guess the word.\n \n\
             1)For guessing the word in first chance '5' points will be awarded \n thereby '-1' word will be deduducted for every attempt.\
             \n 2)For each failed attempt a body part is exhausted. \n 3)When all body parts are exhausted you lose.")
    L8 = Tkinter.Label(game.start, textvariable=var8,font=("times new roman",18))
    L8.pack( side = Tkinter.BOTTOM)
    
    img3 = load_image('hangman-icon.jpg')
    L = Tkinter.Label(game.start, image = img3)
    L.pack(side =Tkinter.TOP,fill = Tkinter.BOTH, )
    
    Button1=Tkinter.Button(game.start,relief="groove",bg="#109070",fg="white",command=Hangman,text="Play" ,font=("copperplate gothic bold",18))
    Button1.pack(side=Tkinter.BOTTOM)
    def destroy(event=None):
            game.start.destroy()
    game.start.bind('<Escape>',destroy)
    game.start.mainloop()

def runa(event=None):#opens intermidiate window
    import Tkinter
    
    import tkMessageBox
    game.start1 = Tkinter.Toplevel()
    
    game.start1.title("Cow and bulls")
    game.start1.minsize(600, 600)
    game.start1.transient(game)

    var8 = Tkinter.StringVar()
    var8.set("The Computer selects a Random four digit Number.Guess the number.\n \n\
             1)For guessing the number number of attempts taken is points awawrded.\
             \n  2)For each failed attempt a cow is shown and on getting four cows you loose.\
             \n 3)For each successful attempt a bull is shown and on getting four bulls you win.")
    L8 = Tkinter.Label(game.start1, textvariable=var8,font=("times new roman",18))
    L8.pack( side = Tkinter.BOTTOM)
             
    img3 = load_image('cowbull-icon.jpg')
    L = Tkinter.Label(game.start1, image = img3)
    L.pack(side =Tkinter.TOP,fill = Tkinter.BOTH)

    Button2=Tkinter.Button(game.start1,relief="groove",bg="#109070",fg="white",command=Cowbull,text="Play" ,font=("copperplate gothic bold",18))
    Button2.pack( side = Tkinter.BOTTOM)
    
    def destroy(event=None):
            game.start1.destroy()
    game.start1.bind('<Escape>',destroy)
    game.start1.mainloop()

def runb(event=None):#opens intermidiate window
    import Tkinter
    
    import tkMessageBox
    game.start2 = Tkinter.Toplevel()
    
    game.start2.title("High or low")
    game.start2.minsize(600, 400)
    game.start2.transient(game)

    var8 = Tkinter.StringVar()
    var8.set("The Computer selects a Random Number between 1 to 50.Guess the number.\n \
             1)For guessing the number , number of attempts taken is points awawrded.\n\
             2)For each 5 attempts you are asked to continue.If you don,t you loose.\n\
             3)For a successful attempt you win.")
    L8 = Tkinter.Label(game.start2, textvariable=var8,font=("times new roman",18))
    L8.pack( side = Tkinter.BOTTOM)
             
    img3 = load_image('mediun.jpg')
    L = Tkinter.Label(game.start2, image = img3)
    L.pack(side =Tkinter.TOP,fill = Tkinter.BOTH)

    Button2=Tkinter.Button(game.start2,relief="groove",bg="#109070",fg="white",command=Highlow,text="Play" ,font=("copperplate gothic bold",18))
    Button2.pack( side = Tkinter.BOTTOM)
    
    def destroy(event=None):
            game.start2.destroy()
    game.start2.bind('<Escape>',destroy)
    game.start2.mainloop()

def runc(event=None):#opens intermidiate window
    import Tkinter
    
    import tkMessageBox
    game.start3 = Tkinter.Toplevel()
    
    game.start3.title("High or low")
    game.start3.minsize(600, 600)
    game.start3.transient(game)

    var8 = Tkinter.StringVar()
    var8.set("The Computer selects a Random four Alphabets.Guess the right alphabets.\n \n\
             1)For guessing the alphabet , number of attempts taken is points awawrded.\
             \n  2)For each wrong attempt you are asked to continue.If you don,t you loose.\
             \n 3)For guessing all four wrong alphabets you loose. \n 4)For guessing all non-forbiden letters you win.")
    L8 = Tkinter.Label(game.start3, textvariable=var8,font=("times new roman",18))
    L8.pack( side = Tkinter.BOTTOM)
             
    img3 = load_image('forbidden-icon.jpg')
    L = Tkinter.Label(game.start3, image = img3)
    L.pack(side =Tkinter.TOP,fill = Tkinter.BOTH)

    Button2=Tkinter.Button(game.start3,relief="groove",bg="#109070",fg="white",command=Forbidletter,text="Play" ,font=("copperplate gothic bold",18))
    Button2.pack( side = Tkinter.BOTTOM)
    
    def destroy(event=None):
            game.start3.destroy()
    game.start3.bind('<Escape>',destroy)
    game.start3.mainloop()

def run1(event=None):
        import tkMessageBox
        tkMessageBox.showinfo( "Creative Commons Lisence", "THIS IS A PRODUCT OF PA Games SSDDR.\n By clicking on I Agree you comply with Creative Commons Lisence\n Games by PA Games is licensed under the \nCreative Commons Attribution-NonCommercial 4.0 International License.\n To view a copy of this license,\n visit http://creativecommons.org/licenses/by/4.0/ or \n send a letter to Creative Commons, PO Box 1866, \n Mountain View, CA 94042, USA.\nYou may use parts of this program with consent to the makers for free.\n\
    The members of PA Games SSDDR include: \n 1.Subrata Sarkar(<subrotosarkar32@gmail.com>) \n \
    2.Dibyendu Das(<dibyendudgp10@gmail.com>) \n 3.Souhardya Sen(<souhardya147@gmail.com>) \n 4.Rajdeep Deogharia(<deogharia.17@gmail.com>) \n \
    5.Debabrata Mukherjee(<debmuk.dm@gmail.com>)")       

gamelabel4 = Tkinter.Label(game,text = '4. FORBIDDEN LETTER:',font=("comic sans ms",20,"bold"))
gamelabel4.pack(side=Tkinter.BOTTOM,anchor='w')
gamelabel3 = Tkinter.Label(game,text = '3. HIGH OR LOW:',font=("comic sans ms",20,"bold"))
gamelabel3.pack(side=Tkinter.BOTTOM,anchor='w')
gamelabel2 = Tkinter.Label(game,text = '2. COWS AND BULLS:',font=("comic sans ms",20,"bold"))
gamelabel2.pack(side=Tkinter.BOTTOM,anchor='w')
gamelabel1 = Tkinter.Label(game,text = '1. HANGMAN:',font=("comic sans ms",20,"bold"))
gamelabel1.pack(side=Tkinter.BOTTOM,anchor='w')
gamelabel = Tkinter.Label(game,text = 'GAMES:',font=("comic sans ms",20,"bold"))
gamelabel.pack(side=Tkinter.BOTTOM)
gamelabel5 = Tkinter.Label(game,bg="#109070",fg="white",text = '                                                  WEBSITE: pagamesltd.blogspot.com                                                    ')
gamelabel5.place(x='0',y='205')

b2=Tkinter.Button(game, text ="CREDITS OF MEMBERS",relief="groove",bg="#FF9940",fg="white", command = run2, font=("comic sans ms",10,"bold"))
b2.place(x= 162,y=227)

b12=Tkinter.Button(game, text ="Lisence",relief="groove",bg="#FF9940",fg="white", command = run1, font=("comic sans ms",10))
b12.place(x= 202,y=264)

class dummypygame:#class object to be used in place of pygame if not available    
        def play(self): pass
        class mixer:#class object to be used in place of pygame.mixer if not available
                True
                def get_init():
                        True
                class Sound(file):#class object to be used in place of pygame.mixer.Sound if not available
                        class play: pass
        class quit: pass
        def load_sound(file):
                print ('Warning, no sound')
                pygame.mixer = None
        class init: pass#class object to be used in place of pygame if not available
        class error: False
try:
    import pygame
    import os.path
    pygame.init()
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    class dummysound:#class object to be used in place of pygame.mixer.Sound if not available
        def play(self): pass
        def mixer(self): pass
    
    def load_sound(file):
        if not pygame.mixer: return dummysound()
        file = os.path.join(main_dir, 'data', file)
        try:
            sound = pygame.mixer.Sound(file)
            return sound
        except pygame.error:
            print ('Warning, unable to load, %s' % file)
            return dummysound()

    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None

    #load the sound effects
    if pygame.mixer:
        music = os.path.join(main_dir, 'data', 'beethoven_fur_elise_orig.mid')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
 
except ImportError:#checks import exception
             print 'pygame not found.Please install and run'
             pygame=dummypygame

class dummysound:#class object to be used in place of pygame.mixer.Sound if not available
        def play(self): pass
        def mixer(self): pass
main_dir = os.path.split(os.path.abspath(__file__))[0]    
def load_sound(file):
        if not pygame.mixer: return dummysound()
        file = os.path.join(main_dir, 'data', file)
        try:
            sound = pygame.mixer.Sound(file)
            return sound
        except pygame.error:
            print ('Warning, unable to load, %s' % file)
            return dummysound()     

def  Hangman(event=None):
    b1.config(state="disabled")
    game.start.destroy()
    
    import random, os.path   
    import main1
    import time
    import Tkinter
    import tkMessageBox
    

    pygame.init()

    #load the sound effects
    loose_sound = load_sound('loose.wav')
    win_sound = load_sound('win.wav')        
    game.top = Tkinter.Toplevel()
    game.top.title("HANGMAN")
    game.top.transient(game)
    game.top.minsize(600, 600)

    #the below code generates a random word
    Word_list=['rain','game','name','mane','good','everytime','ant','baboon',
               'badger','bat','bear','beaver','camel','cat','clam','cobra',
               'cougar','coyote','crow','deer','dog','donkey','duck','eagle',
               'ferret','fox','frog','goat','goose','hawk','lion','lizard',
               'llama','mole','monkey','moose','mouse','mule','newt','otter',
               'owl','panda','parrot','pigeon','python','rabbit','ram','rat',
               'raven','rhino','salmon','seal','shark','sheep','skunk','sloth',
               'snake','spider','stork','swan','tiger','toad','trout','turkey',
               'turtle','weasel','whale','wolf','wombat','zebra']
    ranno=random.randint(0,(len(Word_list)-1))
    word=Word_list[ranno]    
    o=5
    word2=''
    for i in range(len(word)):
        word2+='*'
    x= word2
    wordl=list(word2)
    #=================================================================================
    
    label= Tkinter.Label(game.top, text='HANGMAN',font=("gadzoox",60),bg='#801080',fg='white')
    label.pack(side=Tkinter.TOP)

    var7 = Tkinter.StringVar()    
    L7 = Tkinter.Label(game.top, textvariable=var7,font=("copperplate gothic bold",18))
    L7.pack( side = Tkinter.TOP)

    var8 = Tkinter.StringVar()
    var8.set('Your score is 5 of 5')
    L8 = Tkinter.Label(game.top, textvariable=var8,font=("copperplate gothic bold",18))
    L8.pack( side = Tkinter.BOTTOM)
    
    L1 = Tkinter.Label(game.top, text="Enter a character",font=("comic sans ms",30))
    L1.pack( side =Tkinter.BOTTOM)

    E1 = Tkinter.Entry(game.top, bd =5)
    E1.pack(side = Tkinter.BOTTOM)
    
    L0 = Tkinter.Label(game.top, text="Chances Left",font=("chiller",30),fg='red')
    L0.pack( side = Tkinter.RIGHT)
    
    var1 = Tkinter.StringVar()
    var1.set('5')
    L3 = Tkinter.Label(game.top, text="5",textvariable=var1,font=("chiller",30),fg='red')
    L3.pack( side = Tkinter.RIGHT)
    
    var = Tkinter.StringVar()
    L2 = Tkinter.Label(game.top, text="",textvariable=var,font=("lucida calligraphy",16))
    L2.pack( side = Tkinter.BOTTOM)

    
    L6 = Tkinter.Label(game.top, image = img9,anchor="w")
    L6.place(x=0,y=0)
    
    
    L4 = Tkinter.Label(game.top, image = img)
    L4.pack(side = Tkinter.LEFT,fill = Tkinter.BOTH)
    
    var2 = Tkinter.StringVar()
    var2.set(word2)
    L5 = Tkinter.Label(game.top,bg="#109070",fg="white", textvariable=var2,font=("arial",18,"bold"))
    L5.pack( side = Tkinter.BOTTOM)

    labelp= Tkinter.Label(game.top,text='')
    labelp.place(x=400,y=100)
    #=======================================================================================
    #The below code keeps record of time
    timer = [0, 0]
    pattern = '{0:02d}:{1:02d}'    
    
    def update_timeText():       
        # Every time this function is called,        
        # Every 1000 microsecond is equal to 1 second
        timer[1] += 1
        # Every 60 seconds is equal to 1 min
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1])
        # Update the timeText Label box with the current time
        labelp.configure(text=timeString)
        # Call the update_timeText() function after 1 second
        game.top.after(1000, update_timeText)
    
    def quitee(even=None):#the dialog box tobe showed upon exit by quit buuton
      C.config(state="disabled")
      s=tkMessageBox.askyesno( "Are you sure?", "Click yes to quit")
      if s== True:
          b1.config(state="normal")
          main1.reset()
          game.top.destroy()
      else:
          C.config(state="normal")
    C = Tkinter.Button(game.top,relief="groove",bg="#FF3050",fg="white", text ="QUIT", command = quitee,font=("arial",18,"bold"))

    C.pack(side = Tkinter.BOTTOM)
    #==============================================================================================
    def gettextBack(event=None):#the main works of checking word, etc. is done here       
       letter=E1.get()
       if len(letter)==1:
        displaytext,o,word3,wordl1= main1.mainwork(letter,word,x,wordl)

        var.set(displaytext)
        var2.set(word3)
        var8.set('Your score is '+str(o)+' of5')
        var1.set(o)
       
        if word3==word:
               win_sound.play()               
               var7.set('The word is '+word)
               tkMessageBox.showinfo( "You win", "You are a genius."+"The word was "+word+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec')
               b1.config(state="normal")
               main1.reset()
               game.top.destroy()
               
               
        elif o==4:          
          img2 = load_image('mann2.JPG')
          L4.configure(image = img2)
          L4.image = img2
        elif o==3:
          img3 = load_image('mann3.JPG')
          L4.configure(image = img3)
          L4.image = img3
        elif o==2:
          img4 = load_image('mann4.JPG')
          L4.configure(image = img4)
          L4.image = img4
        elif o==1:
          img5 = load_image('mann5.JPG')
          L4.configure(image = img5)
          L4.image = img5
       
        elif o==0:
           B.config(state ="disabled")
           img6 = load_image('mann6.JPG')
           L4.configure(image = img6)
           L4.image = img6    
           loose_sound.play() 
           var7.set('The word is '+word)
           tkMessageBox.showinfo( "You loose", "Better luck next time!"+"The word was "+word+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec')
           b1.config(state="normal")
           main1.reset()
           game.top.destroy()
           
       else:
           var.set("Enter a single character only.")
       
    
    
    B = Tkinter.Button(game.top,relief="groove",bg="#0060FF",fg="white", text ="OK", command = gettextBack,font=("arial",18,"bold"))

    B.pack(side = Tkinter.BOTTOM)
    if game.top.destroy:
        b1.config(state="normal")
    E1.bind('<Return>', gettextBack)
    game.top.bind('<Escape>',quitee)    
    update_timeText()
    game.top.mainloop()

def Cowbull(event=None):
    b3.config(state="disabled")
    game.start1.destroy()
    
    import random, os.path   
    import increase
    import Tkinter
    import tkMessageBox

    pygame.init()

    #load the sound effects
    loose_sound = load_sound('loose.wav')
    win_sound = load_sound('win.wav')

       
    
    game.top2 = Tkinter.Toplevel()
    
    game.top2.title("COW AND BULL")
    game.top2.minsize(745,550)
    game.top2.transient(game)

    #generating random 4 digit number
    p=0
    number = random.randint(1000,9999)
    #================================================================================
    label= Tkinter.Label(game.top2, text='COW AND BULL',font=("gadzoox",60),bg='#801080',fg='white')
    label.place(x=100,y=0)

        
    L7 = Tkinter.Label(game.top2, text="Guess a four digit number",font=("copperplate gothic bold",18))
    L7.place(x=100,y=100)

    var = Tkinter.StringVar()
    L2 = Tkinter.Label(game.top2, text="",textvariable=var,font=("lucida calligraphy",16))
    L2.place(x=50,y=400)

    var8 = Tkinter.StringVar()
    var8.set('You have taken '+str(p)+' attempts')
    L8 = Tkinter.Label(game.top2, textvariable=var8,font=("copperplate gothic bold",18))
    L8.pack( side = Tkinter.BOTTOM)
    
    img9 = load_image('pagames1.JPG')
    img = load_image('blank.JPG')
    img1 = load_image('blank.JPG')
    L6 = Tkinter.Label(game.top2, image = img9,anchor="w")
    L6.place(x=0,y=0)
    
    L1 = Tkinter.Label(game.top2, image = img1)
    L1.place(x=0,y=200)
    
    L5 = Tkinter.Label(game.top2, image = img)
    L5.place(x=0,y=300)
        
    E1 = Tkinter.Entry(game.top2, bd =5)
    E1.place(x=100,y=150)
    
    var2 = Tkinter.StringVar()
    var2.set('0 bulls')
    L4 = Tkinter.Label(game.top2, text="5",textvariable=var2,font=("chiller",30),fg='blue')
    L4.place(x=410,y=300)
    
    var1 = Tkinter.StringVar()
    var1.set('0 cows')
    L3 = Tkinter.Label(game.top2, text="5",textvariable=var1,font=("chiller",30),fg='#999900')
    L3.place(x=410,y=200)
    #==========================================================================================
    #The below code keeps record of time

    labelp= Tkinter.Label(game.top2,text='')
    labelp.place(x=500,y=250)

    timer = [0, 0]
    pattern = '{0:02d}:{1:02d}'    
    
    def update_timeText():       
        # Every time this function is called,
        # Every 1000 microsecond is equal to 1 second
        timer[1] += 1
        # Every 60 seconds is equal to 1 min
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1])
        # Update the timeText Label box with the current time
        labelp.configure(text=timeString)
        # Call the update_timeText() function after 1 second
        game.top2.after(1000, update_timeText)
    #==================================================================================================
    def quitee(event=None):#the dialog box tobe showed upon exit by quit buuton
      C.config(state="disabled")
      s=tkMessageBox.askyesno( "Are you sure?", "Click yes to quit")
      if s== True:
          b3.config(state="normal")
          increase.reset()
          game.top2.destroy()
      else:
          C.config(state="normal")
    C = Tkinter.Button(game.top2,relief="groove",bg="#FF3050",fg="white", text ="QUIT", command = quitee,font=("arial",18,"bold"))

    C.pack(side = Tkinter.BOTTOM)
    #======================================================================================================
    
    def guessnumber(event=None):#the main work of checking numbers is done here
        guess=E1.get()
        o=increase.increase()
        var.set('')        
        guess_str = str(guess)
        num = str(number)
        length = len(guess_str)
        if length != 4:
            if guess=='':
                var.set('You entered nothing')
            else:
                var.set("You did not enter a 4 digit number.")
                o-=1
        else:
            cows =0
            bulls = 0
            for i in range (4):
                if guess_str[i] == num[i]:
                    bulls += 1
                elif guess_str[i] in num:
                    cows += 1
            var2.set(str(bulls)+"bulls")
            var1.set(str(cows)+"cows")
            if bulls==0:
                img = load_image('blank.JPG')
                L5.configure(image = img)
                L5.image = img
            elif bulls==1:
                img = load_image('bull0.JPG')
                L5.configure(image = img)
                L5.image = img
            elif bulls==2:
                img = load_image('bull1.JPG')
                L5.configure(image = img)
                L5.image = img
            elif bulls==3:
                img = load_image('bull2.JPG')
                L5.configure(image = img)
                L5.image = img
            elif bulls==4:
                img = load_image('bull3.JPG')
                L5.configure(image = img)
                L5.image = img                
            if cows==0:
                img1 = load_image('blank.JPG')
                L1.configure(image = img1)
                L1.image = img1
            elif cows==1:
                img1 = load_image('cow0.JPG')
                L1.configure(image = img1)
                L1.image = img1
            elif cows==2:
                img1 = load_image('cow1.JPG')
                L1.configure(image = img1)
                L1.image = img1
            elif cows==3:
                img1 = load_image('cow2.JPG')
                L1.configure(image = img1)
                L1.image = img1
            elif cows == 4:
                img1 = load_image('cow3.JPG')
                L1.configure(image = img1)
                L1.image = img1                
            if bulls==4 and cows==0:                
                win_sound.play()
                tkMessageBox.showinfo("You win","Hurray!!! You guessed it in"+str(o)+"turns.The number was "+str(number)+" \
  CONGRATS! YOU WIN!"+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec')
                b3.config(state="normal")
                increase.reset()
                game.top2.destroy()
                
            elif cows==4 and bulls==0:
                loose_sound.play()
                tkMessageBox.showinfo("You loose","Sorry you lost..."+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec'+"\n GAME OVER!!!")
                b3.config(state="normal")
                increse.reset()
                game.top2.destroy()
                
            var8.set('You have taken '+ str(o)+ ' attempts')
    #========================================================================================================        
    B = Tkinter.Button(game.top2,relief="groove",bg="#0060FF",fg="white", text ="OK", command = guessnumber,font=("arial",18,"bold"))

    B.place(x=240,y=145)
    if game.top2.destroy:
        b3.config(state="normal")
    E1.bind('<Return>', guessnumber)
    game.top2.bind('<Escape>',quitee)
    update_timeText()
    game.top2.mainloop()

def  Highlow(event=None):
    b4.config(state="disabled")
    game.start2.destroy()
    
    import random, os.path   
    import increase
    import Tkinter
    import tkMessageBox

    pygame.init()

    #load the sound effects
    loose_sound = load_sound('loose.wav')
    win_sound = load_sound('win.wav')
    
    game.top3 = Tkinter.Toplevel()
    game.top3.title("high or low")
    game.top3.transient(game)
    game.top3.minsize(650, 500)

    #the random number between 1 to 50 is generated here
    number=random.randint(1,50)
    
    chance=0

    label= Tkinter.Label(game.top3, text='HIGH OR LOW',font=("gadzoox",60),bg='#801080',fg='white')
    label.place(x=100,y=0)
    
    img9 = load_image('pagames1.JPG')
    L6 = Tkinter.Label(game.top3, image = img9,anchor="w")
    L6.place(x=0,y=0)

    img = load_image('mediun.JPG')
    L4 = Tkinter.Label(game.top3, image = img)
    L4.place(x=0,y=150)

    var1 = Tkinter.StringVar()
    L3 = Tkinter.Label(game.top3, text="5",textvariable=var1,font=("chiller",30),fg='red')
    L3.place(x=0,y=300)

    E1 = Tkinter.Entry(game.top3, bd =5)
    E1.place(x=0,y=350)

    var8 = Tkinter.StringVar()
    var8.set('You have taken '+str(chance)+' attempts')
    L8 = Tkinter.Label(game.top3, textvariable=var8,font=("copperplate gothic bold",18))
    L8.pack( side = Tkinter.BOTTOM)

    #==========================================================================================
    #The below code keeps record of time
    labelp= Tkinter.Label(game.top3,text='')
    labelp.place(x=450,y=250)

    timer = [0, 0]
    pattern = '{0:02d}:{1:02d}'    
    
    def update_timeText():       
        # Every time this function is called,
        # Every 1000 microsecond is equal to 1 second
        timer[1] += 1
        # Every 60 seconds is equal to 1 min
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1])
        # Update the timeText Label box with the current time
        labelp.configure(text=timeString)
        # Call the update_timeText() function after 1 second
        game.top3.after(1000, update_timeText)
    #==============================================================================================
    
    def quitee(even=None):#the dialog box tobe showed upon exit by quit buuton
      C.config(state="disabled")
      s=tkMessageBox.askyesno( "Are you sure?", "Click yes to quit")
      if s== True:
          b4.config(state="normal")
          game.top3.destroy()
          increase.reset()
      else:
          C.config(state="normal")
    C = Tkinter.Button(game.top3,relief="groove",bg="#FF3050",fg="white", text ="QUIT", command = quitee,font=("arial",18,"bold"))

    C.place(x=550,y=350)
    #======================================================================================================
    def play(event=None):#main work of comparing numbeer is done here
        gues=E1.get()
        guess=int(gues)        
        var8.set("")
        num=str(number)        
        chance=increase.increase()        
        if guess>number:
            var1.set("Your guess is higher than the original number")
            img1 = load_image('high.JPG')
            L4.configure(image = img1)
            L4.image = img1
            if chance%5==0:
                g=tkMessageBox.askyesno( "Do you want to play more?", "Click no to quit")
                if g== True:
                    pass
                else:
                    loose_sound.play()
                    tkMessageBox.showinfo("You loose","Sorry you lost... \n GAME OVER!!! The number was"+str(num)+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec')
                    b4.config(state="normal")
                    increase.reset()
                    game.top3.destroy()
        elif guess<number:
            var1.set("Your guess is lower than the original number")
            img2 = load_image('low.JPG')
            L4.configure(image = img2)
            L4.image = img2
            if chance%5==0:
                g=tkMessageBox.askyesno( "Do you want to play more?", "Click no to quit")
                if g== True:
                    pass
                else:
                    loose_sound.play()
                    tkMessageBox.showinfo("You loose","Sorry you lost... \n GAME OVER!!! The number was"+str(num)+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec')
                    b4.config(state="normal")
                    increase.reset()
                    game.top3.destroy()
        elif guess==number:
                win_sound.play()
                tkMessageBox.showinfo("You win","Hurray!!! You guessed it in"+str(chance)+"turns.The number was "+str(num)+" \
  CONGRATS! YOU WIN!"+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec')
                b4.config(state="normal")
                increase.reset()
                game.top3.destroy()                
                        
        var8.set('You have taken '+ str(chance)+ ' attempts')
    #========================================================================================================    
    B = Tkinter.Button(game.top3, text ="OK",relief="groove",bg="#0060FF",fg="white", command = play,font=("arial",18,"bold"))

    B.place(x=150,y=350)
    if game.top3.destroy:
        b4.config(state="normal")
    E1.bind('<Return>', play)
    game.top3.bind('<Escape>',quitee)
    update_timeText()
    game.top3.mainloop()

def  Forbidletter(event=None):
    b5.config(state="disabled")
    game.start3.destroy()

    import random, os.path   
    import increase
    import checkchar
    import Tkinter
    import tkMessageBox
    
    pygame.init()

    #load the sound effects
    loose_sound = load_sound('loose.wav')
    win_sound = load_sound('win.wav')
    
    game.top4 = Tkinter.Toplevel()
    game.top4.title("Forbidden Letter")
    game.top4.transient(game)
    game.top4.minsize(900, 700)

    #The random alphabets generated here
    alLst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
       'S','T','U','V','W','X','Y','Z']
    alLst1=alLst
    c=0
    w=0
    ForLst=[]
    for i in range(4):
        a=random.randint(0,len(alLst)-1)
        ForLst+=alLst1.pop(a)

    chance=0
    
    ForL1=[]
    Lst2=[]
    #==============================================================================================
    label= Tkinter.Label(game.top4, text='DOES IT \n CONTAIN \n FORBIDDEN \n LETTER',font=("gadzoox",60),bg='#801080',fg='white')
    label.place(x=100,y=0)

    var7 = Tkinter.StringVar()    
    L7 = Tkinter.Label(game.top4, textvariable=var7,font=("copperplate gothic bold",18))
    L7.place(x=0,y=450)

    L1 = Tkinter.Label(game.top4, text="Enter a word",font=("comic sans ms",30))
    L1.place(x=400,y=250)

    E1 = Tkinter.Entry(game.top4, bd =5)
    E1.place(x=550,y=310)
    
        
    L6 = Tkinter.Label(game.top4, image = img9,anchor="w")
    L6.place(x=0, y=0)
    
    img56 = load_image('blank1.JPG')
    L4 = Tkinter.Label(game.top4, image = img56)
    L4.place(x=100,y=250)

    var = Tkinter.StringVar()    
    L2 = Tkinter.Label(game.top4, text="",textvariable=var,font=("times new roman",14))
    L2.place(x=0,y=500)

    var8 = Tkinter.StringVar()
    var8.set('You have taken '+str(chance)+' attempts')
    L8 = Tkinter.Label(game.top4, textvariable=var8,font=("copperplate gothic bold",18))
    L8.pack( side = Tkinter.BOTTOM)

    #==========================================================================================
    #The below code keeps record of time    
    labelp= Tkinter.Label(game.top4,text='')
    labelp.place(x=700,y=150)

    timer = [0, 0]
    pattern = '{0:02d}:{1:02d}'    
    
    def update_timeText():       
        # Every time this function is called,
        # Every 1000 microsecond is equal to 1 second
        timer[1] += 1
        # Every 60 seconds is equal to 1 min
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1])
        # Update the timeText Label box with the current time
        labelp.configure(text=timeString)
        # Call the update_timeText() function after 1 second
        game.top4.after(1000, update_timeText)
    #==============================================================================================
        
    def quitee(even=None):#the dialog box tobe showed upon exit by quit buuton
      C.config(state="disabled")
      s=tkMessageBox.askyesno( "Are you sure?", "Click yes to quit")
      if s== True:
          b5.config(state="normal")
          increase.reset()
          checkchar.reset()
          game.top4.destroy()
      else:
          C.config(state="normal")
    C = Tkinter.Button(game.top4,relief="groove",bg="#FF3050",fg="white", text ="QUIT", command = quitee,font=("arial",18,"bold"))

    C.pack(side = Tkinter.BOTTOM)
    #=================================================================================================

    def checkwordf(event=None):#the main work of checking the alphabets is done here  
       letter1=E1.get()
       c=0
       w=0
       var.set('')
       letter1=letter1.upper()
       if len(letter1)>1:
           for q in range(len(letter1)):
               letter=letter1[q]
               
               if letter in ForLst:
                       w+=1
                       chance=increase.increase()
                       var8.set('You have taken '+str(chance)+' attempts')
                       ForL1=checkchar.insForL1(letter)
                       
                       var7.set('The forbidden letters are'+str(ForL1))
                       if len(ForL1)<=4:
                               img57 = load_image('wrong.JPG')
                               L4.configure(image = img57)
                               L4.image = img57
                               if w==len(letter1):
                                       loose_sound.play()
                                       tkMessageBox.showinfo("You loose","Sorry you lost... \n GAME OVER!!! The letters were"+str(ForLst)+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec')
                                       b5.config(state="normal")
                                       increase.reset()
                                       checkchar.reset()
                                       game.top4.destroy()
                      
                               else:
                                       g=tkMessageBox.askyesno( "Do you want to continue?", "This is a Forbidden Letter.Click no to quit")
                                       if g== False:
                                               loose_sound.play()
                                               tkMessageBox.showinfo("You loose","Sorry you lost... \n GAME OVER!!! The letters were"+str(ForLst)+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec')
                                               b5.config(state="normal")
                                               increase.reset()
                                               checkchar.reset()
                                               game.top4.destroy()
               elif letter in alLst:
                  c+=1
                  chance=increase.increase()
                  var8.set('You have taken '+str(chance)+' attempts')
                  img58 = load_image('right.JPG')
                  L4.configure(image = img58)
                  L4.image = img58
                  Lst2=checkchar.insLst2(letter)
                  var.set('The non-forbidden letters are'+str(Lst2))
                  if c==len(letter1):
                      win_sound.play()
                      tkMessageBox.showinfo("You win","Hurray! You win The letters were"+str(ForLst)+"\n You took "+str(timer[0])+'min'+str(timer[1])+'sec')
                      b5.config(state="normal")
                      increase.reset()
                      checkchar.reset()
                      game.top4.destroy()
                
               elif letter=='\n':
                     break
               else:
                   var.set('You entered other than alphabet')
       else:
           var.set("Do not enter a single character.")   
    
    B = Tkinter.Button(game.top4, text ="OK",relief="groove",bg="#0060FF",fg="white", command = checkwordf,font=("arial",18,"bold"))
    B.place(x=600,y=360)
    if game.top4.destroy:
        b5.config(state="normal")
    E1.bind('<Return>', checkwordf)
    game.top4.bind('<Escape>',quitee)
    update_timeText()
    game.top4.mainloop()
b5=Tkinter.Button(game, text ="PLAY",relief="groove",bg="#0060FF",fg="white", command = runc, font=("comic sans ms",12,"bold"))
b5.place(x=334,y=464)
game.bind('<,>',runc)

b4=Tkinter.Button(game, text ="PLAY",relief="groove",bg="#0060FF",fg="white", command = runb, font=("comic sans ms",12,"bold"))
b4.place(x=334,y=419)
game.bind('<;>',runb)

b3=Tkinter.Button(game, text ="PLAY",relief="groove",bg="#0060FF",fg="white", command = runa, font=("comic sans ms",12,"bold"))
b3.place(x=334,y=370)
game.bind('<]>',runa)
b1=Tkinter.Button(game, text ="PLAY",relief="groove",bg="#0060FF",fg="white", command = run, font=("comic sans ms",12,"bold"))
b1.place(x=334,y=323)
game.bind('<[>',run)

b51=Tkinter.Button(game, text ="HELP",relief="groove",bg="#0060FF",fg="white", command = runc, font=("comic sans ms",12,"bold"))
b51.place(x=410,y=464)

b41=Tkinter.Button(game, text ="HELP",relief="groove",bg="#0060FF",fg="white", command = runb, font=("comic sans ms",12,"bold"))
b41.place(x=410,y=419)

b31=Tkinter.Button(game, text ="HELP",relief="groove",bg="#0060FF",fg="white", command = runa, font=("comic sans ms",12,"bold"))
b31.place(x=410,y=370)

b11=Tkinter.Button(game, text ="HELP",relief="groove",bg="#0060FF",fg="white", command = run, font=("comic sans ms",12,"bold"))
b11.place(x=410,y=323)

game.bind('<m>',run2)
game.mainloop()
pygame.quit()

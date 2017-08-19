def binfile():
    import pickle
    file = open('log.dat','wb')
    while True:
         x = bin(int(raw_input()))
         pickle.dump(x,file)
         ans = raw_input('want to enter more data Y / N')
         if ans.upper()== 'N' : break
    file.close()
    file = open('log.dat','rb')
    try :
       while True :
           y = pickle.load(file)
           print y
    except EOFError :
            pass
    file.close()
binfile()

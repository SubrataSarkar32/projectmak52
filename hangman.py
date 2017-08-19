def  Hangman():
    import random
    import man
    import checkword
    print '============================================================'
    print 'HANGMAN'
    print
    print 'Press * any time to quit.Your game starts:'
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
    limit=5
    initi=0
    wordl=list(word)
    o=0    
    newwordl1=[]
    for i in range(len(word)):
            newwordl1+=['*']
    uni2=True
    while uni2==True:
      while initi<=limit:
        a= raw_input('Enter a letter:')
        if a in word:
            print a, 'is in the word.'
            newwordl1=checkword.check(word,a,o,newwordl1)
            man.man(initi)
            if wordl==newwordl1:
                    break
        elif a=='*':
            uni2=False
            break
        else:
            print a, 'is not in the word.'
            initi+=1
            man.man(initi)
        o+=1
      if wordl==newwordl1:
        print 'You win!'
        print 'The word is',word
        uni2=False
      else:
        print 'You loose.'
        print 'Better luck next time.'
        print 'The word is',word
        uni2=False
    print '=========================================================='
           
            

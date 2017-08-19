def check(a,b,c,d):    
    
    for i in range(len(a)):        
        if a[i]==b:            
            d[i]=b
    for j in range(len(a)):
        print d[j],
    print
    return d

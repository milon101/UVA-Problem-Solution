while True:
    n = int(input())
    if n==0:
        break
    s = str(n)
    l = len(s)
    
    s1 = s[:l-1]
    d = int(s1) - int(s[l-1])*5
    if d%17==0:
        print (1)
    else:
        print(0)
        

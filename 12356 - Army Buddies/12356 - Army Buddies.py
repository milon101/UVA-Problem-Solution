while True:
    s, b = [int(n) for n in input().split()]

    if s==0 and b==0:
        break

##-----First Way---------------

    
##    lst = [5]*(s+2)
##
##    for i in range(b):
##        b1, b2 = [int(n) for n in input().split()]
####        print(b1,b2)
##        for i in range(b1, b2+1):
##            lst[i] = 0
####        print(lst)
##
##        c = b1
##        d = b2
##        while(lst[c]!=5):
##            c-=1
##        while(lst[d]!=5):
##            d+=1
##        if c <1:
##            c = '*'
##        if d>s:
##            d = '*'
##        print(c,d)
##    print('-')

##------Second Way----------

##    lst = [i for i in range(s+2)]
##
##    for i in range(b):
##        b1, b2 = [int(n) for n in input().split()]
####        print(b1,b2)
##        for i in range(b1, b2+1):
##            lst.remove(i)
####        print(lst)
##        c = '*'
##        d = '*'
##
##        for i in range(len(lst)-2):
####            print(i+1,lst[i+1],b1)
##            if lst[i+1]<b1:
##                c = lst[i+1]
##                break
####            else:
####                c = '*'
##        for i in range(len(lst)-2):
##            if lst[i+1]>b2:
##                d = lst[i+1]
##                break
####            else:
####                d = '*'
##            
##
##        print(c,d)

##---------Third Way------
    
    LS = []
    RS = []
    for i in range(s+2):
        LS.append(i-1)
        RS.append(i+1)

        c = ''
        d = ''
    for i in range(b):
        b1, b2 = [int(n) for n in input().split()]

        if(LS[b1] <1):
           c = '*'
        else:
            c = LS[b1]

        if(RS[b2] > s):
            d = '*'
        else:
            d = RS[b2]

        LS[RS[b2]] = LS[b1]
        RS[LS[b1]] = RS[b2]

##        print(LS,RS)
        print(c, d)

        

    
    print('-')

        

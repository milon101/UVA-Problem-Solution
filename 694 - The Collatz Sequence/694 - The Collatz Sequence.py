j = 1
while True:
    a,l = map(int,input().split())
    if a==-1 and l==-1:
            break
    i=0
    b = a
    while True:
        if a == 1:
            i+=1
            break
        elif a%2 == 0:
            a = a/2
            i+=1
        elif a%2 != 0:
            a = 3*a + 1
            i+=1
            if a>l:
                break
    print('Case %d: A = %d, limit = %d, number of terms = %d'%(j,b,l,i))
    j+=1

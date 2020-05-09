##def findSwaps( n, a ):
##    b = [n]
##    count = 0
##    for i in range(n):
##        b.append(a[i])
##        
##    for i in range(n):
##        for j in range(n-1):
##            if( b[j] > b[j+1] ):
##                temp = b[j]
##                b[j] = b[j+1]
##                b[j+1] = temp
##                count = count + 1
##    return count
##    
##
##
##n = input()
##n = int(n)
##for i in range(n):
##    s = 0
##    l = []
##    m = input()
##    m = int(m)
##    for j in range(m):
##        l.append(j+1)
##        s+=findSwaps(j+1,l)
##    p = s/m
##    if (p.is_integer()):
##        print ('Case %d: %d'%(i+1,s/m))
##    else:
##        print ('Case %d: %d/%d'%(i+1,s,m))


n = input()
n = int(n)
for i in range(n):
    m = input()
    m = int(m)
    p = m*(m-1)/2
    if (p%2==0):
        print ('Case %d: %d'%(i+1,p/2))
    else:
        print ('Case %d: %d/%d'%(i+1,(m*(m-1)/2),2))
    

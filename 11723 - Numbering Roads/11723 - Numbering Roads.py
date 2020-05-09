import math
i = 1
while True:
    try:
        r,n =input().split()
        r = int(r)
        n = int(n)

        if (n<=0 or r >= 10001):
            break;
        p = ((r-n)/n)
        if (p<=26):
            print('Case %d: %d'%(i,math.ceil(p)))
        else:
            print('Case %d: impossible'%i)
        i = i+1
    except EOFError:
        break

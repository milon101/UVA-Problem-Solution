import math
n = input()
n = int(n)
for i in range(n):
    l = [int(x) for x in input().split()]
    m = l[0]
    m = math.ceil(m/2)
    print ('Case %d: %d'%(i+1,l[m]))
    

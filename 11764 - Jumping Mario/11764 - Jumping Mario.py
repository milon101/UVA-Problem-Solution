t = int(input())
for i in range(t):
    n = int(input())
    lst = [int(x) for x in input().split()]
    hj = 0
    lj = 0
    for j in range(n-1):
        if lst[j]<lst[j+1]:
            hj+=1
        elif lst[j]>lst[j+1]:
            lj+=1
    print ('Case %d: %d %d'%(i+1,hj,lj))

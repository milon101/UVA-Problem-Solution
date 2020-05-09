j = 1
while True:
    n = int(input())
    if n== 0:
        break
    lst = [int(x) for x in input().split()]
    i=0
    for x in lst:
        if x>0:
            i+=1
        else:
            i-=1
    print('Case %d: %d'%(j,i))
    j+=1
    

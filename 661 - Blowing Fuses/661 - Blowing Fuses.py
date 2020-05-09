cnt = 1
while True:
    lst2= [int(x) for x in input().split()]
    n = lst2[0]
    m = lst2[1]
    c = lst2[2]
    if n== 0 and m==0 and c==0:
        break
    elif n == 0:
        print('Fuse was not blown.')
    lst = []
    lst1 = []
    for i in range(n):
        lst.append(int(input()))
        lst1.append(False)

    t = 0
    mx = 0
    print('Sequence %d'%cnt)
    for i in range(m):
        a = int(input())
        if lst1[a-1]==False:
            lst1[a-1] = True
            t+=lst[a-1]
            if t>mx :mx = t
        elif(lst1[a-1] == True):
            lst1[a-1] = False
            t-= lst[a-1]
            
    if c<mx:
        print('Fuse was blown.')
    else:
        print('Fuse was not blown.')
        print('Maximal power consumption was %d amperes.'%mx)
    print()
    cnt+=1

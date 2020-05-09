while True:
    b,n = map(int,input().split())
    if(b+n == 0):
        break
    dic = {}
    lst = [int(x) for x in input().split()]
    for i in range(1,b+1):
        dic[i] = lst[i-1]
    for i in range(n):
        lst1 = [int(x) for x in input().split()]
        dic[lst1[0]] -= lst1[2]
        dic[lst1[1]] += lst1[2]


    for x in dic:
        f = False
        if dic[x]<0:
            print('N')
            break
        else:
            f = True
    if f:
        print('S')

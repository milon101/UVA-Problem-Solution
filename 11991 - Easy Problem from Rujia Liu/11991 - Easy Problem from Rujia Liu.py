while True:
    try:
        n,m = map(int, input().split())
        lst = [int(x) for x in input().split()]
        lst1 = {}
        for i in range(n):
            if (lst[i]) in lst1:
                lst1[lst[i]].append(i)
            else:
                lst1[lst[i]] = [i]
        for i in range(m):
            k,v = map(int,input().split())
            if len(lst1[v])>k-1:
                print(lst1[v][k-1]+1)
            else:
                print(0)
    except EOFError:
        break
        

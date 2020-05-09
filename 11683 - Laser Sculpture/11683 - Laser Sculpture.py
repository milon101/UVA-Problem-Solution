while True:
    a,b = map(int,input().split())
    if a==0 and b == 0:
        break
    lst = [int(x) for x in input().split()]

    n = a - lst[b-1]
    for i in range(b-2,-1,-1):
        if lst[i]<lst[i+1]:
            n += lst[i+1] - lst[i]
    print(n)

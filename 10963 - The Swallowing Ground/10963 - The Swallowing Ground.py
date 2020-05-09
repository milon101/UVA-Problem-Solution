t = int(input())
for i in range(t):
    input()
    n = int(input())
    lst = []
    for j in range(n):
        lst.append([int(x) for x in input().split()])
    x = lst[0]
    a = x[0] - x[1]

    f = True
    for y in lst:
        b = y[0] - y[1]
        if a!=b:
            f = False
            break
    if f:
        print('yes')
    else:
        print('no')
    if (i!=t-1):
        print()

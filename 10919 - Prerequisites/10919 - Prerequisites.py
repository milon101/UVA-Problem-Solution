while True:
    lst = [int(x) for x in input().split()]
    if lst[0] == 0:
        break
    lst1 = [int(x) for x in input().split()]

    lst2 = []
    for i in range(lst[1]):
        lst2.append([int(x) for x in input().split()])

    f = True
    for i in range(lst[1]):
        x = lst2[i]
        k = 0
        f = True
        for j in range(x[0]):
            if (x[j+2] in lst1):
                k+=1
        if k < x[1]:
            f = False
            break
    if f:
        print('yes')
    else:
        print('no')

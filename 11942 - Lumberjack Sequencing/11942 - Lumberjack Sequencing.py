n = int(input())
print('Lumberjacks:')
for i in range(n):
    lst = [int(x) for x in input().split()]

    a = True
    for j in range(9):
        if (lst[j]>=lst[j+1]):
            a = False
            break

    if(a==False):
        a = True
        for j in range(9):
            if lst[j]<=lst[j+1]:
                a = False
                break
    if a:
        print('Ordered')
    else:
        print('Unordered')

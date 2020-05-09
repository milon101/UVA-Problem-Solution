t = int(input())
for i in range(t):
    lst = []
    for j in range(10):
        lst.append([x for x in input().split()])
    for x in lst:
        x[1] = int(x[1])
    lst.sort(key=lambda x: x[1],reverse = True)
    v = lst[0]
    print ('Case #%d:'%(i+1))
    print(v[0])
    for j in range(1,10):
        x = lst[j]
        if v[1] == x[1]:
            print(x[0])

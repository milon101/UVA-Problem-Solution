n = input()
n = int(n)
for i in range(n):
    m = input()
    m = int(m)
    keys = []
    values = []
    for j in range(m):
        key, value = input().split()
        keys.append(key)
        values.append(value)
    k = input()
    k = int(k)
    lst = ''
    for j in range(k):
        lst += input()
    s = 0
    for x in lst:
        for y in range(len(keys)):
            if(keys[y]==x):s += int(values[y])
    print('%.2f$'%(s/100))

n = int(input())
for k in range(n):
    input()
    amp = int(input())
    freq = int(input())
    for f in range(freq):
        lst = []
        s = ''
        for i in range(1,amp+1):
            for j in range(1,i+1):
                s+=str(i)
            lst.append(s)
            s = ''
        for i in range(len(lst)):
            print(lst[i])
        for i in range(len(lst)-2,-1,-1):
            print(lst[i])
        if f!=(freq-1):
            print()
    if (k!=(n-1)):
        print()


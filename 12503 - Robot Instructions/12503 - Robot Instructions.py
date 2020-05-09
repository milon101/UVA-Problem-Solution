t = int(input())
for i in range(t):
    lst = []
    n = int(input())
    for j in range(n):
        m = input()
        if( m == 'LEFT' or m== 'RIGHT'):
            lst.append(m)
        else:
            b = int(m[8:])
            lst.append(lst[b-1])
    p = 0
    for x in lst:
        if x == 'LEFT':
            p-=1
        elif x == 'RIGHT':
            p+=1
    print(p)

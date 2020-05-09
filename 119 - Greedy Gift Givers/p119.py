lst = []
while True:
    try:
        m = input()
    except EOFError:
        break
    n = int(m)
    dicto = {}
    frnd = input().split()
    for i in frnd:
        dicto[i] = 0
        
    for i in range(n):
        a = input().split()
        b = int (a[1])
        c = int (a[2])
        if c==0:
            continue
        d = int (b/c)
        dicto[str(a[0])] += -(b-(b - (c*d)))
        for j in range(c):
            dicto[str(a[j+3])] += d

    for i in frnd:
        if i == frnd[n-1]:
            s =(str(dicto[i]) + '\n')
            lst.append(str(i)+' ' + s)
            break
        lst.append(str(i)+ ' '+ str(dicto[i]))
        
lst[len(lst)-1] = lst[len(lst)-1].strip()
for i in range(len(lst)):
    print (lst[i])

lst = []
while True:
    try:
        n = int(input())
        lst.append(n)
    except EOFError:
        for i in range(0,len(lst)-1,2):
            a = lst[i]
            b = lst[i+1]
            c = a*b
            print(c)
        break

while True:
    n = int(input())
    if n == 0:
        break
    s = str(n)
    while(len(s)>1):
        f = 0
        for x in s:
            f+= int(x)
            s = str(f)
    print(s)

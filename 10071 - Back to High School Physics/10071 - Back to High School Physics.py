while True:
    try:
        a,b = map(int,input().split())
        if a==0 or b == 0:
            print(0)
        else:
            print(a*b*2)

    except EOFError:
        break

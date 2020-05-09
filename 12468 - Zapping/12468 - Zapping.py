while True:
    a,b = map(int,input().split())
    if(a==-1 and b==-1):
        break

    if (abs(100+a - b)>abs(a-b)):
        if(abs(a-b))>abs((b+100)-a):
            print(abs((b+100)-a))
        else:
           print(abs(a-b))
    else:
        print(abs(100+a-b))

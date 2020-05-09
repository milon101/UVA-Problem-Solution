d = 1
while True:
    try:
        s = input().strip()
        if not s:
            break
        lst = [0]
        for i in range(1,len(s)+1):
            lst.append( lst[i-1] +int(s[i-1]))
        n = int(input())
        print('Case %d:' %d)
        d+=1
        for i in range(n):
            f = False
            a,b  = map(int,input().split())
            if a==b:
                print('Yes')
                continue
            if (a>b):
                temp=a
                a=b
                b=temp
            a+=1
            b+=1

            if(lst[b] - lst[a-1] == 0 or lst[b] - lst[a-1] == b-a+1):
                print('Yes')
            else:
                print('No')
        
    except EOFError:
        break

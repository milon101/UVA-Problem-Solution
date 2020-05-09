while True:
    n = int(input())
    if n == 0:
        break
    s = input().strip()
    mn = n
    
    if 'Z' in s:
        mn = 0
    else:
        r,d = 0,0
        for i,v in enumerate(s):
            if v=='R':
                r = i+1
            elif v=='D':
                d = i+1

            if r and d:
                dist = abs(r-d)
                if dist < mn:
                    mn = dist
    print(mn)

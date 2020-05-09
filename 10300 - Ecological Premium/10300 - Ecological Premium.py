n = int(input())
for i in range(n):
    f = int(input())
    out = 0
    for j in range (f):
        a,b,c = map(int,input().split())
        out+=(a*c)
    print(out)
        

n = int(input())

for i in range(n):
    a,b,c = map(int,input().split())
    if (a<=20 and b<=20 and c<=20):
        print("Case %d: good"%(i+1))
    else:
        print('Case %d: bad'%(i+1))

t = int(input())
for i in range(1,t+1):
    a = int(input())
    b = int(input())
    total = 0
    for j in range(a,b+1):
        if j%2!=0:
            total+=j
    print('Case %d: %d'%(i,total))

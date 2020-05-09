T = int(input().strip())
for _ in range(1,T+1):
    d, v, u = map(int,input().split())
    if u<=v or u<=0 or v <= 0:
        print("Case %d: can't determine"%_)
    else:
        T1 = d/(u**2 - v**2)**(1/2)
        T2 = d/u

        print("Case %d: %.3f"%(_,T1-T2))

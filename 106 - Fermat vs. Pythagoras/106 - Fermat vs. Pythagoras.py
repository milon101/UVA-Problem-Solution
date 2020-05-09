from math import gcd

while True:
    try:
        n = int(input())
        m = int(n**(1/2))
        lst=[0 for i in range(n+1)]
        tri = 0
        total = 0
        if (m*m<n):
            m+=1
        for r in range(1,m+1):
            up = min((n - r*r),r-1)
            for s in range(1,up+1):
                x = r*r - s*s
                y = 2*r*s
                z = r*r + s*s
                if(x*x + y*y == z*z and z<=n):
                    if gcd(x,y) == 1:
                        tri = tri+1
                        k = 1
                        while(k*z<=n):
                            lst[k*x] = 1
                            lst[k*y] = 1
                            lst[k*z] = 1
                            k+=1

        for k in range(1,n+1):
            if lst[k]==0:
                total+=1
                lst[k] = 0
        print(tri,total)
                        

    except EOFError:
        break

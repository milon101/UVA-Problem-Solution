import math
while True:
    
    lst = [int(x) for x in input().split()]
    if lst[0]==0 and lst[1]==0 and lst[2]==0 and lst[3]==0 and lst[4]==0:
        break
    M = lst[0]*lst[3]
    N = lst[1]*lst[4]
    V = ((M*M+N*N)**(1/2))/lst[2]
    A = math.atan(N/M)*(180/math.pi)
    print('%.2f %.2f' %(A, V))

case = 1
while True:
    n,q = map(int,input().split())
    if n==0 and q == 0:
        break
    lst_n = []
    lst_q = []
    for i in range(n):
        lst_n.append(int(input()))
    for i in range(q):
        lst_q.append(int(input()))
        
    lst_n.sort()

    print('CASE# %d:'%case)
    for i in range(len(lst_q)):
        k = 0
        for j in range(len(lst_n)):
            if lst_q[i] == lst_n[j] and k!=1:
                print('%d found at %d'%(lst_q[i],j+1))
                k = 1
                break
        if k ==0:
            print('%d not found'%lst_q[i])

    case+=1

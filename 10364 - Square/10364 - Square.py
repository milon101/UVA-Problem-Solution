n = int(input())
for i in range(n):
    lst = [int(x) for x in input().split()]
    lst.remove(lst[0])
    c = 0
    if(sum(lst)%4 == 0):
        for j in range(len(lst)):
            for k in range(len(lst)):
                if k==j:
                    continue
                if (lst[j]+lst[k]) == (sum(lst)/4):
                    c+=1
        if c ==8 or c == 0:
            print('yes')
        else:
            print('no')
    else:
        print('no')

n = int(input())
for i in range(n):
    l = int(input())
    lst = [int(x) for x in input().split()]
    k=0
    for u in range(l):    
        for j in range(l-1):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
                k+=1
    print('Optimal train swapping takes %d swaps.'%k)

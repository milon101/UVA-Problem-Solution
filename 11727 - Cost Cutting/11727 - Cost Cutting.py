n = int(input())
for i in range(n):
    lst = [int(x) for x in input().split()]
    lst.sort()
    print('Case %d: %d'%(i+1,lst[1]))

n = int(input())
j=0
for i in range(n):
    lst = input().split()
    if lst[0]=='report':
        print(j)
    else:
        j+=int(lst[1])

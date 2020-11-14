n = int(input())
lst = []

for i in range (n):
    x = (input().split())
    for i in range(1,len(x)):
        x[i] = int(x[i])
    lst.append(x)
lst = sorted(lst, key=lambda t: t[::-1])
print(lst[len(lst)-1][0])
print(lst[0][0])

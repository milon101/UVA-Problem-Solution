n = int(input())
for i in range(n):
    a = int(input())
    b = [int(x) for x in input().split()]
    b.sort()
    c = (b[a-1]-b[0])*2
    print(c)

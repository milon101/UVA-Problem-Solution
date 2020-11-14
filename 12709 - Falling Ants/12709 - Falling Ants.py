while True:
    n = int(input())
    maxH = -1
    maxV = -1
    if n==0:
        break
    for i in range(n):
        l, w, h = [int(i) for i in input().split()]
        v = l* w * h
        if h > maxH or (h== maxH and v>maxV):
            maxH = h
            maxV = v
    print(maxV)

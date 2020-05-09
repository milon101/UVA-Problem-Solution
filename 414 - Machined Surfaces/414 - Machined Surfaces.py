while True:
    n = int(input())
    if n==0:
        break
    lst = []
    longest = 0
    for i in range(n):
        s = input()
        if longest<s.count('X'):
            longest = s.count('X')
        lst.append(s)
    t = 0
    for x in lst:
        t += longest - x.count('X')
    print(t)

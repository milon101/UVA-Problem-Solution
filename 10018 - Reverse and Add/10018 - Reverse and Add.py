def check(s):
    if s == s[::-1]:
        return True
    return False

n = int(input())
for i in range(n):
    s = input()
    j = 0
    while(check(s)!=True):
        rs = s[::-1]
        a = int(s)
        b = int(rs)
        s = str(a+b)
        j+=1
    print(j,s)

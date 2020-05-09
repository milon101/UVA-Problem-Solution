def initialize(n):
    return [-1 for i in range(n)]

def fib(n, li):
    if li[0] == -1:
        li[0] = 1
    if li[1] == -1:
        li[1] = 2
    if li[n] == -1:
        li[n] = fib(n - 1, li) + fib(n - 2, li)
    return li[n]

def biggest_f(m):

    n = 1
    prev = 1
    temp = 1
    s = 0
    if m==0:
        return m
    for i in range(m-1,-1,-1):
        temp = n
        n+=prev
        prev  = temp
        if n>m:
            break
    return prev

li = initialize(201)
fib(200, li)

while True:
    try:
        
        n1 = input().strip()[::-1]
        n2 = input().strip()[::-1]

        if n1 == '0' and n2 == '0':
            print("0")
        else:
            n1 = sum(li[i] for i in range(len(n1)) if n1[i] == '1')
            n2 = sum(li[i] for i in range(len(n2)) if n2[i] == '1')
            n = n1 + n2
            
        m = biggest_f(n)
        ix = -1
        for i in range(len(li)-1):
            if li[i]==m:
                ix = i
                break
            
        res = []
        while ix >= 0:
            if n >= li[ix]:
               res.append('1')
               n -= li[ix]
            else:
                res.append('0')
            ix -= 1
        print(''.join(res).lstrip('0'))
        input()
        print()
    except EOFError:
        break

import math
lst = []
med = 0
while True:
    try:
        n = int(input().strip())
        lst.append(n)
        lst= sorted(lst)
        l = len(lst)
##        print(lst)
        if l%2==0 and l>1:
            m = int(l/2)
##            print(m,l)
            med = (lst[m-1] + lst[m])/2
        elif l == 1:
            med = n
        else:
            m = math.ceil(l/2)
            med = lst[m-1]
        print(math.floor(med))

    except EOFError:
        break

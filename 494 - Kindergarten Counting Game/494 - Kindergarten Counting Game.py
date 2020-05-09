while True:
    try:
        n = input().strip()
        flag = 0
        count = 0
        for x in n:
            if x.isalpha():
                flag = 1
            else:
                count+=flag
                flag = 0
##        z = ''.join(e for e in n if (e.isalpha() or e ==' '))
##        m = z.split()
        print(count)
    except EOFError:
        break

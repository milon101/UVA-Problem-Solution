lst = []
while True:
    try:
        s = input().strip()
        lst.append(s)
    except EOFError:
        for x in lst:
            print(x)
            st = x.split(" ")
##            print(st)
            if(int(st[0]) > (2 ** 31 - 1)):
                print('first number too big')
            if(int(st[2]) > (2 ** 31 - 1)):
                print('second number too big')
            if(( st[1]=='+' and int(st[0])+ int(st[2]) > (2 ** 31 - 1)) or (st[1]=='*' and int(st[0]) * int(st[2]) > (2 ** 31 - 1))) :
                print('result too big')
        break


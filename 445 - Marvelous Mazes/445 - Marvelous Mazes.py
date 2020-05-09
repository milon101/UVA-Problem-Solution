while True:
    try:
        s = input()
        if s == '':
            print()
            continue
        f = 0
        lst = []
        lst1 = []
        g = ''
        for x in range(len(s)):
            if s[x]=='!' or s[x]== '\n':
                lst1.append(g)
                g = ''
            elif x==len(s)-1:
                g+=s[x]
                lst1.append(g)
            elif s[x] == 'b':
                g+=' '
            else:
                g+=s[x]

        y = ''
        for s in lst1:
            for i in s:
                if i.isdigit():
                    f+=int(i)
                elif i.isalpha() or i==' ' or i=='*':
                    for j in range(f):
                        y+=i
                    f = 0
            lst.append(y)
            y = ''
        for x in lst:
            print(x)
    except EOFError:
        break

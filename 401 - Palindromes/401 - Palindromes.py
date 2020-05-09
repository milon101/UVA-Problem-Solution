while True:
    try:
        p = False
        t = False
        dic = {'A':'A',
               'E':'3',
               'H':'H',
               'I':'I',
               'J':'L',
               'L':'J',
               'M':'M',
               'O':'O',
               'S':'2',
               'T':'T',
               'U':'U',
               'V':'V',
               'W':'W',
               'X':'X',
               'Y':'Y',
               'Z':'5',
               '1':'1',
               '2':'S',
               '3':'E',
               '5':'Z',
               '8':'8'}
        
        s = input()
        if s==s[::-1]:
            p = True
            
        s1 = ''
        s2 = s[::-1]
        for x in s2:
            if x in dic:
                s1+=dic[x]
        if s1==s:
            t = True
        if p and t:
            print('%s -- is a mirrored palindrome.'%s)
        elif p and not t:
            print("%s -- is a regular palindrome." %s)
        elif t and not p:
            print("%s -- is a mirrored string." %s)
        else:
            print("%s -- is not a palindrome." %s)
        print()
    except EOFError:
        break
    

import string
while True:
    try:
        chars = [x for x in string.ascii_uppercase]
        char_to_ix = { ch:i for i,ch in enumerate(chars) }
        n = input()
        m = input()
        n = n.upper()
        m = m.upper()

        s = 0
        t = 0
        a = 0
        b = 0
        for x in n:
            if x in chars:s += int(char_to_ix[x])+1
        for x in m:
            if x in chars:t += int(char_to_ix[x])+1
        num1 = [int(x) for x in str(s)]
        num2 = [int(x) for x in str(t)]
        while(True):
            for x in num1:a += x
            for x in num2:b += x
            s = a
            t = b
            num1 = [int(x) for x in str(s)]
            num2 = [int(x) for x in str(t)]
            
            if (len(num1)==1 & len(num2)==1):break
            a = 0
            b = 0 
        if (a<b):print('%.2f %%'%(a/b*100))
        else:print('%.2f %%'%(b/a*100))
    except EOFError:
        break

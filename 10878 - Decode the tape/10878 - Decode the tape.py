def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

##s1 = 'Hello, World!'
##b = string2bits(s1)
##s2 = bits2string(b)

t = 0
lst = []
while True:
    s = input()
    if s == '___________' and t>0:
        st = ''
        for x in lst:
            st += bits2string(x)
        print(st.strip())
        break
    elif s != '___________':
        s = s.strip('|')
        s = s[:5]+s[6:]
        for i in range(len(s)):
            if s[i] == 'o':
                s = s[:i] + '1'+ s[i+1:]
            elif s[i] == ' ':
                s = s[:i] + '0' + s[i+1:]
        lst.append([s])
        t+=1
    
        

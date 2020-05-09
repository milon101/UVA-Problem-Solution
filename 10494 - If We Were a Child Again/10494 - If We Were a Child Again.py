import math
while True:
    try:
        s = input().strip().split(' ')
        rem = 0
    except EOFError:
        break
    s1 = s[0]
    if (s[1]=='/'):
        flag = 1
        lst = []
        for i in range(len(s1)):
            rem = int(s1[i])+ rem * 10
            if(rem / int(s[2])):
                flag = 0
            if (flag == 0):
                lst.append(math.floor(rem / int(s[2])))
            rem = rem % int(s[2])
        s2 = ''
        for x in lst:
            s2 = s2 + str(x)
        print(s2.lstrip('0'))
        if flag == 1:
            print(0)
    if (s[1]=='%'):
        print(int(s[0])%int(s[2]))
        

import math
n = int(input())
s = ['Happy', 'birthday', 'to', 'you', 'Happy', 'birthday', 'to', 'you', 'Happy', 'birthday', 'to', 'Rujia', 'Happy', 'birthday', 'to', 'you']
lst = []
for i in range(n):
    lst.append(input())
k = 0
l = 0
if len(lst)>16:
    for i in range(0,math.ceil(n/16)*16):
        if (k>=16):
            k = 0
        elif (l>=n):
            l = 0
        print('%s: %s'%(lst[l],s[k]))
        k+=1
        l+=1
else:
    for i in range(0,len(s),3):
        for j in range(len(lst)):
            if(i+j < len(s)):
                print('%s: %s'%(lst[j],s[i+j]))

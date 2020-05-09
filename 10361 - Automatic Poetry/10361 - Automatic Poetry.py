n = int(input())
for i in range(n):
    s = input()
    ss = input().strip('.')
    j = 0
    lst = []
    while True:
        if j == len(s) - 1:
            if s[j]=='>' and len(lst)<4:
                lst.append(j)
            break
        if s[j] == '<':
            lst.append(j)
        if s[j] == '>':
            lst.append(j)
        j+=1
    s1 = s[:lst[0]]
    s2 = s[lst[0]+1:lst[1]]
    s3 = s[lst[1]+1:lst[2]]
    s4 = s[lst[2]+1:lst[3]]
    s5 = s[lst[3]+1:len(s)]
    
    print(s1+s2+s3+s4+s5)
    print(ss+s4+s3+s2+s5)

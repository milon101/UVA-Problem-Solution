n = int(input())
for i in range(n):
    s = input()
    lst = []
    lst1 = []
    for j in range(len(s)):
        s1=''
        if s[j] == '=':
            k = j+1
            while True:
                s1+=s[k]
                if s[k] == 'W' or s[k] == 'V' or s[k] == 'A':
                    if s[k-1] == 'M':
                        s2 = s[j+1:k-1]
                        s1 = str(float(s2)*1000000.0)+s[k]
                    elif s[k-1] == 'k':
                        s2 = s[j+1:k-1]
                        s1 = str(float(s2)*1000.0)+s[k]
                    elif s[k-1] == 'm':
                        s2 = s[j+1:k-1]
                        s1 = str(float(s2)*.001)+s[k]
                    break
                k+=1
            lst.append([s[j-1],s1])
    x = lst[0]
    y = lst[1]
    lx = len(x[1])-1
    ly = len(y[1])-1
    I = 0
    U = 0
    P = 0
    if x[0] == 'U':
        U = float(x[1][:lx])
    if x[0] == 'I':
        I = float(x[1][:lx])
    if x[0] == 'P':
        P = float(x[1][:lx])
    if y[0] == 'I':
        I = float(y[1][:ly])
    if y[0] == 'U':
        U = float(y[1][:ly])
    if y[0] == 'P':
        P = float(y[1][:ly])
    if x[0] == 'U' and y[0] == 'I' or y[0] == 'U' and x[0] == 'I':
        P = U*I
        print('Problem #%d' %(i+1))
        print('P=%.2fW'%P)
        print()
    elif x[0] == 'P' and y[0] == 'I' or y[0] == 'P' and x[0] == 'I':
        U = P/I
        print('Problem #%d' %(i+1))
        print('U=%.2fV'%U)
        print()
    if x[0] == 'U' and y[0] == 'P' or y[0] == 'U' and x[0] == 'P':
        I = P/U
        print('Problem #%d' %(i+1))
        print('I=%.2fA'%I)
        print()
##    print(lst)
            

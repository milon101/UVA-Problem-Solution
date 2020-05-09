t = int(input())
for i in range(t):
    n = int(input())
    dct = {}
    for j in range(1,n+1):
        dct [j] = [j]
##    print(dct)
    while True:
        s = input().split()
##        print(s)
        if s[0] == 'O':
            break
        elif s[0] == 'E':
            val = 0
            for i in range(len(dct[int(s[1])])-1):
                value = abs(dct[int(s[1])][i] - dct[int(s[1])][i+1])%1000
                val += value
##                print(value,val)
            print(val)
        elif s[0] == 'I':
            dct[int(s[1])].append(int(s[2]))
            for key in dct.keys():
                if int(s[1]) in dct[key]:
                    dct[key].append(int(s[2]))
            
##        print(dct)

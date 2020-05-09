n = int(input())
for i in range(n):
    s = input().strip()
    if(s=="1" or s=="4" or s=="78"):print('+')
    elif(s[len(s)-1]=='5' and s[len(s)-2]=='3'):
        print("-")
    elif(s[len(s)-1]=='4' and s[0]=='9'):
        print("*")
    elif(s[0]=='1' and s[1]=='9' and s[2]=='0'):
        print("?")

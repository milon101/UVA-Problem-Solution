n = int(input())
for i in range (n):
    s = input()
    j = 0
    if len(s) == 5:
        print(3)
    elif (('o'== s[0] and 'n' == s[1]) or ('n' == s[1] and 'e' == s[2]) or ('o' == s[0] and 'e' == s[2])):
        print(1)
    else:
        print(2)
        
        

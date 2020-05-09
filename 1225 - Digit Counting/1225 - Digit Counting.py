n = int(input())
for i in range(n):
    m = int(input())
    s = ''
    for i in range(1,m+1):
        s+=str(i)
    print(s.count('0'),s.count('1'),s.count('2'),s.count('3'),s.count('4'),s.count('5'),s.count('6'),s.count('7'),s.count('8'),s.count('9'))

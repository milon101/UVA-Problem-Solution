string = ''
while True:
    s = input().strip()
    if s == '#':
        break
    string += ' '+s+' '
lst = string.split()
lst1 = []
for i in range(len(lst)):
    word = lst[i].lower()
    s1 = ''.join(sorted(word))
    flag = False
    for j in range(len(lst)):
        word1 = lst[j].lower()
        s2 = ''.join(sorted(word1))

        if s1 == s2 and i!=j:
            flag = True
            break
    if flag == False:
        lst1.append(lst[i])
for x in sorted(lst1):
    print(x)

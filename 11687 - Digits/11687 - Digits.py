while True:
    x = input()
    if x == 'END':
        break
    elif x=='1':
        print(1)
        continue
    lst = []
    lst.append(len(x))
    lst.append(len(str(lst[-1])))
    while(lst[len(lst)-1]!=lst[len(lst)-2]):
        lst.append(len(str(lst[-1])))
    print(len(lst))

while True:
    try:
        lst = [int(x) for x in input().split()]

        n = lst[0]
        lst1 = []
        for i in range(n-1):
            lst1.append(abs(lst[i+1] - lst[i+2]))

        flag = True
        for x in range(n-1):
            if x+1 not in lst1:
                flag = False
                break
                
        if (flag):print('Jolly')
        else:print('Not jolly')
            
    except EOFError:
        break

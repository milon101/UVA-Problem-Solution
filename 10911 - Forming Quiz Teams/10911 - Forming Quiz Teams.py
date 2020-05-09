k = 1
while True:
    n = int(input())
    if n==0:
        break

    def distance(lst):
        dist = ((lst[0]-lst[2])**2 + (lst[1] - lst[3])**2)**(1/2)
        return dist

    def takeSecond(elem):
        return elem[2]

    def lowest_dist(lst):
        lst1 = []
        for i in range (len(lst)):
            x = lst[i]
            if i in lst2:
                continue
            for j in range(i+1,len(lst)):
                y = lst[j]
                if j in lst2:
                    continue
                dist = distance([int(x[1]),int(x[2]),int(y[1]),int(y[2])])
                lst1.append([i,j,dist])

        lst1.sort(key=takeSecond)    
        return lst1


    lst = []
    lst1 = []
    lst2 = []
    for i in range(n*2):
        lst.append(input().split())
    lst3 = lowest_dist(lst)


    sum_lst = []
    for x in lst3:
        sum1 = 0.0
        lst4 = []
        for w in range(len(lst3)):
            z = lst3[w]
            if x == z and n!=1:
                continue
            if z[0] in lst4 or z[1] in lst4:
                continue
            sum1+=float(z[2])
            lst4.append(z[0])
            lst4.append(z[1])
        if(len(lst4)!=n*2):
            continue
        sum_lst.append(sum1)

    sum_lst.sort()
    print('Case %d: %.2f'%(k,sum_lst[0]))
    k+=1

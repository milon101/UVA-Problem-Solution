def degree(frm,to,direction):
    if direction == "C":
        if frm < to:
            deg = abs((frm+40) - to)
        else:
            deg = abs(frm - to)
    elif direction == 'CC':
        if frm > to:
            deg = abs(frm - (to+40))
        else:
            deg = abs(frm - to)
    return deg*9

while True:
    lst = [int(x) for x in input().split()]
    flag  = False
    a=0
    b=(360*3)
    i = 0
    a=lst[i]+lst[i+1]+lst[i+2]+lst[i+3]
    if a==0:
        break
    for i in range(len(lst)-1):
        if i % 2==0:
            b+=degree(lst[i],lst[i+1],'C')
        else:
            b+=degree(lst[i],lst[i+1],'CC')
    print(b)

t = int(input())
for i in range(t):
    Mile = 0
    Juice = 0
    n = int(input())
    lst = [int(x) for x in input().split()]
    for x in lst:
        Mile+=int((x/30)+1)
        Juice+=int((x/60)+1)
    Mile = Mile*10
    Juice=Juice*15
    if(Mile<Juice):
        print('Case %d: Mile %d'%(i+1,Mile))
    elif(Mile>Juice):
        print('Case %d: Juice %d'%(i+1,Juice))
    else:
        print('Case %d: Mile Juice %d'%(i+1,Mile))
        

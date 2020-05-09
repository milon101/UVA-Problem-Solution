
l = 1
while True:
    n,p = map(float,input().split())
    if(n+p == 0):
        break
    for i in range(int(n)):
        input()
    lst = []
    best_compliance = 0
    best_cost = 0
    best_name = ''
    for i in range(int(p)):
        x = input()
        y = ([float(v) for v in input().split()])
        if(y[1]/p > best_compliance or y[1]/p == best_compliance and y[0]<best_cost):
            best_compliance = float(y[1]/p)
            best_cost = y[0]
            best_name = x
        for j in range(int(y[1])):
            input()
            
    if l>1:
        print()
    print('RFP #%d'%l)
    l+=1
    print(best_name)
    
    

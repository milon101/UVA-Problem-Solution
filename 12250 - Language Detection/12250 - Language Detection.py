i =1
while True:
    n = input().strip()
    if n == '#':
        break
    elif n =='HELLO':
        print('Case %d: %s'%(i,'ENGLISH'))
    elif n =='HOLA':
        print('Case %d: %s'%(i,'SPANISH'))
    elif n =='HALLO':
        print('Case %d: %s'%(i,'GERMAN'))
    elif n =='BONJOUR':
        print('Case %d: %s'%(i,'FRENCH'))
    elif n =='CIAO':
        print('Case %d: %s'%(i,'ITALIAN'))
    elif n =='ZDRAVSTVUJTE':
        print('Case %d: %s'%(i,'RUSSIAN'))
    else:
        print('Case %d: %s'%(i,'UNKNOWN'))
    i+=1

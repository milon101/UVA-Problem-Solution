import sys 
while(1):
    try:
        R,n = input().split()
    except:
        break
    n = int(n)
    index = R.find('.')
    #print(index)
    dotPos = (5-index)*n 
##    print(dotPos)
    R = int(R.replace('.',''))
    #print(R)
    R = str(pow(R, n))
    #print(R)
    left = R[:-dotPos]
    #print(left)
    right = R[-dotPos:]
    if len(right)!=dotPos:
        e = dotPos-len(right)
        s = ''
        for i in range(e):
            s+='0'
        right = s+right
    
    print('%s.%s'%(left,right.rstrip('0')))

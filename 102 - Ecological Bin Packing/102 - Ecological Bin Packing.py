### using Brute-Force

while True:
    try:
        lst = [int(x) for x in input().split()]

        BGC = sum(lst)-lst[0] - lst[4] - lst[8]
        BCG = sum(lst)-lst[0] - lst[5] - lst[7]
        GBC = sum(lst)-lst[1] - lst[3] - lst[8]
        GCB = sum(lst)-lst[1] - lst[5] - lst[6]
        CBG = sum(lst)-lst[2] - lst[3] - lst[7]
        CGB = sum(lst)-lst[2] - lst[4] - lst[6]
        m = BCG
        
        s = 'BCG'
        i = 0
        l = []

        if m>BCG:
            m = BCG
            s = 'BCG'
            
        if m>BGC:
            m = BGC
            s = 'BGC'

        if m>CBG:
            m = CBG
            s = 'CBG'

        if m>CGB:
            m = CGB
            s = 'CGB'
            
            
        if m>GBC:
            m = GBC
            s = 'GBC'
            
        if m>GCB:
            m = GCB
            s = 'GCB'
            
            
        print('%s %d'%(s,m))
        
    except EOFError:
        break

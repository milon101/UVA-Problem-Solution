from collections import defaultdict

while (True):
       n = int(input())
       if n == 0:
           break
       lst = []
       dic = defaultdict(int)
       r = 0
       flag = False
       for i in range(n):
           s = [int(n) for n in input().split()]
           v = i+s[1]
           if v not in lst and v>=0 and v <= (n-1):
               lst.append(v)
           else:
               r = -1
               if flag == False:
                   print(r)
               flag = True
               continue
           dic[s[0]] = i+s[1]
       dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
       if r!=-1:
           print(*dic.keys())

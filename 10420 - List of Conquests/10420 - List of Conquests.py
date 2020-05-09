n = int(input())
dic = {}
for i in range(n):
    s = input().strip().split()
    if s[0] not in dic:
        dic[s[0]]=1
    else:
        dic[s[0]]+=1
for key in sorted(dic):
    print ("%s %d" % (key, dic[key]))

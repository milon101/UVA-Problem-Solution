import queue as Q

q = Q.PriorityQueue()

lst = []
while True:
    s = input().strip().split()
    if s[0] == '#':
        break
    
    s1 = [int(s[1]), int(s[2])]
    q.put((s1[1], s1[0]))
    lst.append(s1)
n = int(input())

j = 2
while n>0:
    print(q.get()[1])
    for x in lst:
        q.put((j*x[1],x[0]))
    n-=1
    j+=1

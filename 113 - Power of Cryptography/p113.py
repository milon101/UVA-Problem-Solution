import math
while True:
    try:
        n = int(input())
        p = int(input())
        k = round(pow(p,1/n))
        print (k)
    except (EOFError):
        break

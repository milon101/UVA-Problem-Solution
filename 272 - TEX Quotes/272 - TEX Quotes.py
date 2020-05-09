import sys
i = 0
while True:
    try:
        n = input()
        for x in n:
            if x=='"':
                if i%2 == 0:
                    sys.stdout.write("``")
                else:
                    sys.stdout.write("''")
                i+=1
            else:
                sys.stdout.write("%c"%x)
        sys.stdout.write('\n')
    except EOFError:
        break

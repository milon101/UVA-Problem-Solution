def Main():
    try:
        cs=1
        while True:
            s=input()
            a=[s]
            while True:
                s=input()
                if s=='9':
                    break
                a.append(s)
            flag=0
            for s in a:
                for t in a:
                    if s!=t and s.startswith(t):
                        flag=1
            if flag==1:
                print("Set %d is not immediately decodable"%cs)
            else:
                print("Set %d is immediately decodable"%cs)
            cs+=1
    except EOFError:
        return 0
if __name__=="__main__":
    Main()

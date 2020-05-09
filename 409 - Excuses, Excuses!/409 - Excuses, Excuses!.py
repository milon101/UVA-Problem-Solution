def excuse_score(excuse, words):
    
    excuse = excuse.lower()
    len_excuse = len(excuse)

    sdx, edx = 0, 0
    excuse_words = set()
    for jdx in range(len_excuse):
        if jdx == 0 and excuse[0].isalpha():
            sdx = 0
        elif not excuse[jdx-1].isalpha() and excuse[jdx].isalpha():
            sdx = jdx

        if excuse[jdx-1].isalpha() and not excuse[jdx].isalpha():
            edx = jdx
            excuse_word = excuse[sdx:edx]
            if excuse_word in words:
                excuse_words.add(excuse_word)

    if edx != len_excuse - 1 and excuse[len_excuse-1].isalpha():
        excuse_word = excuse[sdx:len_excuse]
        if excuse_word in words:
            excuse_words.add(excuse_word)
    print(excuse_words)
    return len(excuse_words)


c = 1
while True:
    try:
            
        k,e = map(int,input().split())
        keyword = []
        excuse = []
        for i in range(k):
            word = input().lower()
            keyword.append(word)
        for i in range(e):
            excuse.append(input().strip())
        j = 0
        lst = []
        max_counter = 0
        for i in range(len(excuse)):
            j = excuse_score(excuse[i],keyword)
            if j>max_counter:
                max_counter = j
                lst = [excuse[i]]
            elif j==max_counter:
                lst.append(excuse[i])
        print('Excuse Set #%d'%c)
        for i in range(len(lst)):
            print(lst[i])
        print()
        c+=1
    except EOFError:
        break

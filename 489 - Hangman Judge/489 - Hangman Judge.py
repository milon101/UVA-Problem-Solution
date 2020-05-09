while True:
    case = int(input())
    if case == -1:
        break
    puzzle = input().strip()
    guess = input().strip()
    
    print('Round %d'%case)
    flag = 0
    for i in range(len(guess)):
        if puzzle:
            size = len(puzzle)
            puzzle = puzzle.replace(guess[i],'')
            if size == len(puzzle):
                flag+=1
        else:
            break
        
    if not puzzle and flag < 7:
        print("You win.")
    elif puzzle and flag < 7:
        print("You chickened out.")
    else:
        print("You lose.")
    

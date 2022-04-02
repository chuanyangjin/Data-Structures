def PuzzleSolve(k,S,U):
    for i in range(len(U)):
        if U[i] == None:
            continue
        n = U[i]
        U[i] = None
        S.append(n)
        if k == 1:
            print(S)
        else:
            PuzzleSolve(k-1,S,U)
        U[i] = n
        S.remove(n)

U = [1,2,3,4,5]
PuzzleSolve(3,[], U)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
def solution(matrix):
    row = len(matrix)
    col = len(matrix[0])
    start = 0


    rstack = set()
    cstack = set()


    while start < row:
        scol = 0
        while scol < col:
            if matrix[start][scol] == 0:
                rstack.add(start)
                cstack.add(scol)
            scol += 1
        start += 1


    for i in rstack:
        j = 0
        while j < col:
            matrix[i][j] = 0
            j += 1
    for i in cstack:
        j = 0
        while j < row:
            matrix[j][i] = 0
            j += 1
    return matrix

print(solution(matrix))

# 566. Reshape the Matrix

mat = [[1,2],[3,4]]
r = 1
c = 4

def solution(mat, r, c):
    o_r = len(mat)
    o_c = len(mat[0])

    if o_r * o_c != r * c:
        return mat
    
    new_mat = [[0] * c for _ in range(r)]

    i = 0
    while i < (r*c):
        o_row, o_col = i // o_c, i % o_c
        
        n_r, n_c = i // c, i % c

        new_mat[n_r][n_c] = mat[o_row][o_col]
        i += 1
    return new_mat


genrated = solution(mat, r, c)
print(genrated)


ans = [[1,2,3,4]]

if genrated == ans: print(True)
else: print(False)
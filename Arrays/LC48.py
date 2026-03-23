# LC 48 Rotate Image by 90 degree
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

def solution(matrix):
    r = len(matrix)
    l = 0
    while l < r:
        i = l + 1
        while i < r:
            matrix[l][i], matrix[i][l] = matrix[i][l], matrix[l][i]
            i += 1
        matrix[l].reverse()
        l += 1
    print(matrix)
    return 0



print(solution(matrix))
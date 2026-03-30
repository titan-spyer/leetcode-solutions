# LC: 74. Search a 2D Matrix

qes = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

def solution(matrix):
    target = 13
    if not matrix or not matrix[0]:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = (rows * cols) - 1
    while left <= right:
        m = left + (right - left) // 2
        mid_val = matrix[m // cols][m % cols]
        if mid_val == target:
            return True
        elif mid_val < target:
            left = m + 1
        else:
            right = m - 1
    return False


genrated = solution(qes)
print(genrated)


ans = 3

if genrated == ans: print(True)
else: print(False)
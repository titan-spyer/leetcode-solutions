# 54. Spiral Matrix
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def solution(matrix):
    if not matrix:
        return 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    top = 0
    left = 0
    answer = []
    while top <= bottom and left <= right:
        # Travers Top Row 
        tleft = left
        while tleft <= right:
            answer.append(matrix[top][tleft])
            tleft += 1
        top += 1
        # Traverse Right Column 
        ttop = top
        while ttop <= bottom:
            answer.append(matrix[ttop][right])
            ttop += 1
        right -= 1
        # Traverse bottom row 
        if top <= bottom:
            tright = right
            while tright >= left:
                answer.append(matrix[bottom][tright])
                tright -= 1
            bottom -= 1
        # Traverse Left Column 
        if left <= right:
            tbottom = bottom
            while tbottom >= top:
                answer.append(matrix[tbottom][left])
                tbottom -= 1
            left += 1
    return answer

print(solution(matrix))
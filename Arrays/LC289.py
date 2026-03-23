# 289. Game of Life

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

def solution(board):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    row = len(board)
    col = len(board[0])
    r = 0

    while r < row:
        c = 0
        while c < col:
            alive = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < row and 0 <= nc < col:
                    if abs(board[nr][nc]) == 1:
                        alive += 1
            if board[r][c] == 1:
                if alive < 2 or alive > 3:
                    board[r][c] = -1
            else:
                if alive == 3:
                    board[r][c] = 2
            c += 1
        r += 1
    
    r = 0
    while r < row:
        c = 0
        while c < col:
            if board[r][c] == -1:
                board[r][c] = 0
            elif board[r][c] == 2:
                board[r][c] = 1
            c += 1
        r += 1
    return board


genrated = solution(board)
print(genrated)


ans = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

if genrated == ans: print(True)
else: print(False)
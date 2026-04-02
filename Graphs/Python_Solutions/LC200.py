# LC 200 Number of Island
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def solution(grid):
    if not grid:
        return 0
    rows = len(grid)
    colums = len(grid[0])
    island = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r in range(rows):
        for c in range(colums):
            if grid[r][c] == '1':
                island += 1
                stack = [(r, c)]
                grid[r][c] = '0'
                while stack:
                    x, y = stack.pop()

                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy

                        if 0 <= nx <= rows and 0 <= ny < colums:
                            if grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                stack.append((nx, ny))
    return island
        
print(solution(grid))
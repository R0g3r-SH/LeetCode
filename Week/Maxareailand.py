
def isvalid(grid, visited, r, c):
    if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])):
        return False
    elif grid[r][c] == 0:
        return False
    elif visited[r][c] == True:
        return False

    return True


def DFS(grid, sr, sc, visited):

    maxarea = 0

    cols = [0, 1, 0, -1]
    rows = [-1, 0, 1, 0]

    que = [[sr, sc]]

    while (len(que) > 0):

        cur = que[len(que)-1]
        que.remove(que[len(que)-1])
        r = cur[0]
        c = cur[1]

        if isvalid(grid, visited, r, c) == False:
            continue

        maxarea += 1
        visited[r][c] = True

        for i in range(4):
            newrows = r+rows[i]
            newcols = c+cols[i]
            que.append([newrows, newcols])

    return maxarea


def maxAreaOfIsland(grid):
    maxarea = 0
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0:
                maxarea = max(maxarea, DFS(grid, row, col, visited))

    return maxarea


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

max = maxAreaOfIsland(grid)
print(max)

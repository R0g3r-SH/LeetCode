from collections import deque as queue
# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]


def isValid(vis,row,col):
    #inbounds
    if (row < 0 or col < 0 or row >= 3 or col >= 3):
        return False
    if (vis[row][col]):
        return False
    return True


def BFS (grid,vis,row,col):
    q=queue()
    mainS=""

    q.append((row,col))
    vis[row][col] = True
    while (len(q)>0):
        cell = q.popleft()
        x= cell[0]
        y = cell[1]
        print(grid[x][y],end=' ')
        mainS += str(grid[x][y]) +" "

        for i in range(4):
            adjx = x+ dRow[i]
            adjy = y+ dCol[i]
            if isValid(vis,adjx,adjy):
                q.append((adjx,adjy))
                vis[adjx][adjy] = True
                

def floodFill(image):
    vis = [[ False for i in range(4)] for i in range(4)]
    BFS(image, vis, 1, 1)


grid= [[1,1,1],[1,1,0],[1,0,1]]

floodFill(grid)
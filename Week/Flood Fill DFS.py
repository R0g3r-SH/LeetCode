



def isValid(row, col, img,target,vis):
    ROW = len(img)
    COL = len(img[0])
    if (row < 0 or col < 0 or row >= ROW or col >= COL or img[row][col] != target):
        return False
    if (vis[row][col]):
        return False
    return True




def DFS(grid,row,col, color,vis):
    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]
    target = grid[row][col]

    st = []
    st.append([row, col])


    while (len(st) > 0):
        # Pop the top pair
        curr = st[len(st) - 1]
        st.remove(st[len(st) - 1])
        row = curr[0]
        col = curr[1]

        if (isValid(row, col,grid,target ,vis) == False):
            continue

        vis[row][col] = True
        grid[row][col] = color

        for i in range(4):
            adjx = row + dRow[i]
            adjy = col + dCol[i]
            st.append([adjx, adjy])


def floodFill(image , sr,sc,color):
    vis = [[False for i in range(len(image[0]))] for j in range(len(image))]
    DFS(image, sr, sc, color ,vis)
    return image


grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1],[1, 0, 1]]

print(floodFill(grid,1,1,2))


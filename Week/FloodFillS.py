
from hmac import new


def isvalid  (image,r,c,target,visited):
    #limts
    if (r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != target):
        return False
    if (visited[r][c]):
        return False
    return True




def DFS (image, sr,sc,color,target,visited):
    col = [0,1,0,-1]
    row = [-1,0,1,0]

    que = [[sr,sc]]

    while (len(que)>0):

        cur = que[len(que)-1]
        que.remove(que[len(que)-1])
        r = cur[0]
        c = cur[1]

        if isvalid (image,r,c,target,visited) == False:
            continue

        image[r][c] = color
        visited [r][c] = True

        for i in range (4):
            newr = r+row[i]
            newcol = c+col[i]

            que.append([newr,newcol])

def floodFill(image, sr, sc, color):
    visited = [[ False for j in range(len(image[0]))] for i in range(len(image))]
    target = image[sr][sc]
    DFS (image, sr,sc,color,target,visited)
    for i in image:
        print(i)
        
    return image

image = [[0,3,0],[0,0,0]]
sr = 0
sc = 0
color = 1

floodFill(image, sr, sc, color)


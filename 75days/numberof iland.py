
import collections

def isVisited (visited,grid,x,y):

    if (x<0 or y<0 or x>=len(visited) or y>= len(visited[0]) or visited[x][y] ==True or grid[x][y] != "1" or grid[x][y] == "0"):
        return True
    return False



def BFS (grid,visited,sr,sc):

    counter = 0
    nextpos= [  [1,0],
                [-1,0],
                [0,-1],
                [0,1]]
    que = collections.deque()
    que.append([sr,sc])

    while (que):
        currpoint = que.pop()
        currx = currpoint[0]
        curry = currpoint[1]
        if isVisited (visited,grid,currx,curry):
            continue
        counter +=1
        visited[currx][curry] = True
        #create  more points
        for i in range(len(nextpos)):
            newx =  currx + nextpos[i][0]
            newy = curry + nextpos[i][1]
            que.append([newx,newy])

    return counter







            




def numIslands(grid):
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

    maxcount = 0

    for i in range(len (grid)):
        for j in range (len(grid[0])):
            if not isVisited(visited,grid,i,j):
                BFS(grid,visited,i,j)
                maxcount+=1
            else:
                continue

    return maxcount


grid =  [["1","0","1","1","0","0","1","1"]]

print(numIslands(grid))
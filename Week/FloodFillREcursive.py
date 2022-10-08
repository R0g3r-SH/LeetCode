
def recursiveDFS (image, sr,cs,color,rows, cols,target):
    #array limits
    if (sr<0 or sr >= rows or cs < 0 or cs >=cols):
        return

    #the same color
    elif(image[sr][cs] != target):
        return;

    image[sr][sc] = color
    
    recursiveDFS (image, sr-1,cs,color,rows, cols,target)
    recursiveDFS (image, sr+1,cs,color,rows, cols,target)
    recursiveDFS (image, sr,cs-1,color,rows, cols,target)
    recursiveDFS (image, sr,cs+1,color,rows, cols,target)
    #recursive calls




def floodFill(image, sr, sc, color):
    if(color == image[sr][sc]):
        return image
    
    rows = len(image)
    cols = len(image[0])
    target = image[sr][sc]

    recursiveDFS(image, sr, sc, color, rows,cols,target)
    return image

image = [[0,3,0],[0,3,0]]
sr = 0
sc = 1
color = 2

print(floodFill(image, sr, sc, color))

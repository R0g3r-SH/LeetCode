def finder(nums, target):
    l = 0
    r = len(nums)-1

    while (l <= r):
        m = (l+r)//2
        mid = nums[m]
        if mid == target:
            return True
        elif mid < target:
            l = m+1
        else:
            r = m-1

    return False

    


def searchMatrix(matrix, target):
    ptr = len(matrix[0])-1
    ptrr = 0

    while ptrr < len(matrix):
        val = matrix[ptrr][ptr]
        if val == target:
            return True
        elif val > target:
            if finder(matrix[ptrr], target):
                return True
        ptrr += 1

    return False


matrix = [[1, 3, 5]]
target = 1

print(searchMatrix(matrix, target))

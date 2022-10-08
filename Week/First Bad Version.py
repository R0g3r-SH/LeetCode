def isBadVersion(n):
    tresh = 4

    if n < tresh:
        return False
    else:
        return True








def firstBadVersion(n):

    l = 1
    r = n
    mid = r+l//2
    res= n

    while (l<=r):
        mid = (r+l)//2
        valm = isBadVersion(mid)
        if valm:
            res = mid
            r = mid-1
        else:
            l = mid+1

    return res  
    

print(firstBadVersion(5))
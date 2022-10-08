def searchInsert(nums, target):
    l = 0 
    r = len(nums)-1
        
    while l<=r:
            
        m = (l+r)//2
        val = nums[m]
            
        if val == target:
            return m
        elif val < target:
            l=m+1
        else:
            r=m-1
    return l


nums = [1,3,5,7]
target = 6
print(searchInsert(nums, target))
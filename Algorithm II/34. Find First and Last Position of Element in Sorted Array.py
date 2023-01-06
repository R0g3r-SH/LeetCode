def finder (m,nums,target):
    l = m
    r = m

    val = nums[l]
    var = nums[r]

    while (l > 0 and val==target  ):
            l-=1
            val = nums[l]
    
    while (r < len(nums)-1 and var==target):
            r+=1
            var = nums[r]
    
    if l == 0 and val==target:
        l=-1
    if r == len(nums)-1 and var==target:
        r = len(nums)
    
    return [l+1,r-1]


def searchRange(nums, target) :

    #using binary search
    print(len(nums))

    if len(nums) == 1 and target == nums[0]:
        return [0,0]
    elif len(nums) == 1 and target != nums[0]:
        return [-1,-1]

    l =0 
    r = len(nums)-1

    while(l<=r):
        m = (l+r)//2
        mid = nums[m]
        if mid == target:
            #find the ends
            return finder(m,nums,target)
        elif mid < target:
            l = m+1
        else:
             r = m-1

    return [-1,-1]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target) )
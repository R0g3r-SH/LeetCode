def pivotIndex(nums):
    
    leftsidesum = 0 
    totalsum = sum(nums)
    piv = 0

    while (piv<len(nums)-1):  
        rigthside = totalsum - nums[piv] - leftsidesum

        if rigthside == leftsidesum:
            return piv

        leftsidesum += nums[piv]
        piv+=1

    return -1

nums = [-1,-1,-1,-1,0,0]
print(pivotIndex(nums))
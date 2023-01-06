def findPeakElement(nums):

    l = 0

    for i in range(1, len(nums)):
        if nums[l] > nums[i]:
            return l
        l += 1
    return len(nums)-1

print(findPeakElement([1,4,4,1]))
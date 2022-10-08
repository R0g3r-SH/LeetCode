


def moveZeroes(nums) -> None:
    ptr = 0
    
    while ptr <len(nums):
        val = nums[ptr]
            
        if val != 0:
            ptr2= ptr
            while (ptr2-1)>=0 and nums[ptr2-1] == 0:
                nums[ptr2-1] ,nums[ptr2] = nums[ptr2], nums[ptr2-1]
                ptr2-=1
                    
        ptr+=1
    return nums


nums = [0,1,0,3,12]
print(moveZeroes(nums))

#Solve prefix and postfix
def productExceptSelf(nums):

    res = [1] * (len(nums))
    prefix =1 

    for i in range(len(nums)):
        res[i] = prefix
        prefix *=nums[i]
    
    postfix =1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]

    return res



nums= [1,2,3,4]
print(productExceptSelf(nums))
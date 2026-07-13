class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]*len(nums)
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
    
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1]* prefix[i-1]
        for j in range(len(nums)-2,-1, -1):
            postfix[j] = nums[j+1]*postfix[j+1]
        for k in range(len(nums)):
            products[k] = prefix[k]*postfix[k]
        return products
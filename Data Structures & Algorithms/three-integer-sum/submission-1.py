class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)
        for idx, num in enumerate(nums):
            left = idx + 1
            right = len(nums) -1

            if idx > 0 and nums[idx] == nums[idx -1]:
                continue
            
            while left < right:

                if num + nums[left] + nums[right] == 0:
                    results.append([num, nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left+ 1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif num + nums[left] + nums[right] < 0:
                    left +=1
                
                elif num + nums[left] + nums[right] > 0:
                    right -=1 
        
        return results

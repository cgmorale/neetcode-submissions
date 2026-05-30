class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        count = 0
        for n in nums:
            numsDict[n] = count
            count +=1
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numsDict:
                if numsDict[difference]!= i:
                    return [i, numsDict[difference]]
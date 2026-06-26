class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} 
        buckets = [[] for i in range(len(nums) + 1)] 
        resultList = []
        for num in nums: 
            if num in freq: 
                freq[num]+=1 
            else: 
                freq[num] = 1 
        for num, count in freq.items():
            buckets[count].append(num)

        for i in range(len(nums), -1, -1):
            resultList.extend(buckets[i])
            if len(resultList) >= k:
                return resultList[:k]
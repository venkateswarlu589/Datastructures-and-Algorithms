class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hashmap:
                return [i,hashmap[value]]
            hashmap[nums[i]] = i
        
        
        
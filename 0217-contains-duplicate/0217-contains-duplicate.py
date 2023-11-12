class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        hashmap = {}
        for i in range(length):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
        for i in hashmap.values():
            y = 0
            maxi = max(y,i)
            if maxi > 1:
                return True
        return False
        
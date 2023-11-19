class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        for key,val in hashmap.items():
            if val > 1:
                break
        return key
        
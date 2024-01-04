class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        count = 0
        for key,val in hashmap.items():
            if val == 1:
                return -1
        for key,val in hashmap.items():
            count += val // 3
            if val % 3:
                count += 1
        return count
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        x, y = 0, 0
        for i in range(len(nums)):
            z = max(nums[i] + x,y)
            x = y
            y = z
        return y
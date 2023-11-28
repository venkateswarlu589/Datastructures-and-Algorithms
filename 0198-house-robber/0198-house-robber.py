class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1= 0
        rob2 = 0
        for i in nums:
            new = max(rob1 + i ,rob2)
            rob1 = rob2
            rob2 = new
        return rob2
       
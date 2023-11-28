
class Solution:
        
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper1(nums),self.helper2(nums))
        
    def helper1(self,nums):
        rob1 = 0
        rob2 = 0
        for i in range(len(nums)-1):
            new = max(rob1 + nums[i],rob2)
            rob1 = rob2
            rob2 = new
        return rob2
    def helper2(self,nums):
        rob1= 0
        rob2 = 0
        for j in range(1,len(nums)):
            new = max(rob1 + nums[j],rob2)
            rob1 = rob2
            rob2 = new
        return rob2
        
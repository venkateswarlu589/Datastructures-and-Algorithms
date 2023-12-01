class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []
        def dfs(i):
            if i >= len(nums):
                result.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return result
            
                
        
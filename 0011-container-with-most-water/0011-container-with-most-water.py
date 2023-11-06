class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left,right = 0,len(height) - 1
        while left < right:
            area = (right-left) * min(height[right],height[left])
            answer = max(area,answer)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer
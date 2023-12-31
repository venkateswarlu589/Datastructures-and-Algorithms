class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxii = -1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    maxii = max(maxii,j-i-1)
        return maxii
                    
        
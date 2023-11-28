class Solution:
    def countSubstrings(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                stack.append(s[i:j])
        count = 0
        for i in stack:
            x = i[::-1]
            if i == x:
                count += 1
        return count
        
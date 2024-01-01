class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        index = 0
        cnt = 0
        
        while index < len(s) and cnt < len(g):
            if s[index] >= g[cnt]:
                cnt += 1
            index += 1
            
        return cnt
        
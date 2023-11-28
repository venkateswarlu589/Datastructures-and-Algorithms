class Solution:
    def shortestPalindrome(self, s: str) -> str:
        sub_str = s[::-1]
        x = ""
        n = len(s)
        for i in range(n):
            a = s[0:n-i]
            b = sub_str[i:]
            if a != b:
                x += a[-1]
            else:
                break
        return x + s
        
        
        # p = s[::-1]
        # add = ""
        # n = len(s)
        # for i in range (n):
        #     a = s[0:n-i]
        #     b = p[i:]
        #     if (a!=b):
        #         add+=a[-1]
        #     else:
        #         break
        # return add+s
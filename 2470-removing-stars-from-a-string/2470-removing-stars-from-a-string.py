class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        string = ""
        for j in stack:
            string += j
        if len(stack) == 0:
            return ""
        return string
        
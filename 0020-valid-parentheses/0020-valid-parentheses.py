class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        string = "({["
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(")")
            elif s[i] == "{":
                stack.append("}")
            elif s[i] == "[":
                stack.append("]")
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == s[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


        
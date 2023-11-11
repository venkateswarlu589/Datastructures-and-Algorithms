class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def track(open,close):
            if open == close == n:
                result.append("".join(stack))
                return 
            if open < n:
                stack.append("(")
                track(open + 1,close)
                stack.pop()
            if close < open:
                stack.append(")")
                track(open,close+1)
                stack.pop()
        track(0,0)
        return result
        
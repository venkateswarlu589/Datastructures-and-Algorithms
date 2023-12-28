class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.n = len(s)
        self.dp = [[-1] * (k + 1) for _ in range(self.n)]
        return self.helper(0, k, s)

    def helper(self, i: int, k: int, s: str) -> int:
        if k < 0:
            return self.n
        if self.n <= i + k:
            return 0

        ans = self.dp[i][k]
        if ans != -1:
            return ans
        ans = self.helper(i + 1, k - 1, s)
        length, same, diff = 0, 0, 0

        for j in range(i, self.n):
            if diff > k:
                break
            if s[j] == s[i]:
                same += 1
                if same <= 2 or same == 10 or same == 100:
                    length += 1
            else:
                diff += 1
            ans = min(ans, length + self.helper(j + 1, k - diff, s))

        self.dp[i][k] = ans
        return ans
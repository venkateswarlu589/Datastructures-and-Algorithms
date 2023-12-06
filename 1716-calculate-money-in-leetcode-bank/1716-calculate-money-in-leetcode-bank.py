class Solution:
    def totalMoney(self, n: int) -> int:
        sum = 1
        total = 1
        sol =0
        for i in range(1,n+1):
            sol += total
            total += 1
            if i % 7 == 0:
                sum += 1
                total = sum
        return sol
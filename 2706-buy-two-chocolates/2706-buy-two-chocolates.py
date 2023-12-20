class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        ans=money-sum(sorted(prices)[:2])
        if ans>=0:
            return ans

        return money 
        
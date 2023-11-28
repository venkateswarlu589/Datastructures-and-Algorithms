class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        vector<vector<int>> curr(2, vector<int> (k + 1, 0)), next(2, vector<int> (k + 1, 0));
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int buy = 0; buy < 2; buy++) {
                curr[buy][0] = 0;
                for (int count = k; count >= 1; count--) {
                    if (buy) {
                        curr[buy][count] = max(-prices[ind] + next[0][count], next[1][count]);
                    } else {
                        curr[buy][count] = max(prices[ind] + next[1][count - 1], next[0][count]);
                    }
                }
            }
            next = curr;
        }
        return curr[1][k];
    }
};
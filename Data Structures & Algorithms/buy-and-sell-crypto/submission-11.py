class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(n-1):
            if i == n-1:
                break
            max_diff = max(prices[i:n]) - prices[i]
            if max_diff <= 0:
                continue
            else:
                max_profit = max(max_profit,max_diff)
                print(max_profit)
        return max_profit
                

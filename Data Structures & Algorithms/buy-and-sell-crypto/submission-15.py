class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l,r = 0,1
        # l is buy, r is sell.
        while l < r:
            if r >= len(prices):
                break
            if prices[l] > prices[r]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
 
            r += 1
        return max_profit
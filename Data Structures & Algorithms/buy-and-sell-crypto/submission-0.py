class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left - buy pointer
        # right - sell pointer
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[right] - prices[left] >= 0:
                max_profit = max(max_profit, prices[right] - prices[left])
                right += 1
            else:
                left += 1
        
        return max_profit



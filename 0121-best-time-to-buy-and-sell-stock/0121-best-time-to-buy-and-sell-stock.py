class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        j = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[j] :
                profit = max(profit,(prices[i] - prices[j]))
            else : j = i
        return profit    
        
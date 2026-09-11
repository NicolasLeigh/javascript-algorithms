class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]

            if diff > 0:
                total += diff

        return total
    

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = -prices[0]
        cash = 0

        for price in prices[1:]:
            prev_hold = hold
            prev_cash = cash

            hold = max(prev_hold, prev_cash - price)
            cash = max(prev_cash, prev_hold + price)

        return cash

# 贪心 - Best
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
    
# 动态规划
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = -prices[0]
        cash = 0

        for price in prices[1:]:
            prev_hold = hold

            hold = max(hold, -price)
            cash = max(cash, price + prev_hold)

        return cash
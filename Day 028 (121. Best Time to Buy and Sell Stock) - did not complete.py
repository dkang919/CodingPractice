class Solution:
    def maxProfit(self,prices):

        left = 0 #Buy
        right = 1 #Sell

        max_profit = 0

        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit


# solution by mageshyt

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy = prices[0]
        max_profit = 0

        for price in prices:
            if(price>buy):
                max_profit=max(max_profit,price-buy)
            else:
                buy=price

        return max_profit

## another solution
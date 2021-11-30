class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0

        lastprice=prices[0]
        profit=0
        for price in prices:
            if price>lastprice:
                profit += price - lastprice
            lastprice=price
        return profit
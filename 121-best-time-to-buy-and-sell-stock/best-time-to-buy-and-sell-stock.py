class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bprice = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < bprice:
                bprice = price
            
            profit = max(profit, price - bprice)
        
        return profit

        

            
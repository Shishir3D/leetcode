class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer = 0
        right_pointer = 1
        maxx = 0

        for i in range(len(prices) - 1):
            if prices[right_pointer] < prices[left_pointer]:
                left_pointer = right_pointer
                right_pointer += 1
            else:
                maxx = max(prices[right_pointer] - prices[left_pointer], maxx)
                right_pointer += 1
        

        return (maxx)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        max_hour, total_hour = r, 0

        while l <= r:
            m = (r + l) // 2
            total_hour = 0
            for pile in piles:
                each_hour = math.ceil(pile / m)
                total_hour += each_hour #time taken to eat bananas
            
            if total_hour > h:
                l = m + 1
            elif total_hour <= h:
                max_hour = m
                r = m -1

        return max_hour

            

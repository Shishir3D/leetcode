class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r

        while l <= r:
            m = (l + r) // 2
            total_hour = 0
            for pile in piles:
                # Calculate the number of hours needed to eat this pile at speed m
                total_hour += math.ceil(pile / m)
            
            if total_hour > h:
                # If total hours exceed h, we need to increase the speed (k)
                l = m + 1
            else:
                # If total hours are within the limit, we try to reduce the speed
                min_k = m
                r = m - 1

        return min_k

            

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []
        frequency = []

        for index, value in enumerate(nums):
            if value not in mp:
                mp[value] = 1
            else:
                mp[value] = mp[value] + 1

        for i in range(k):
            maxx = -100001
            for key, value in mp.items():
                if value > maxx:
                    maxx = value
                    max_key = key

            mp[max_key] = -100003
            res.append(max_key)
            

        return res



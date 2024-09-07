class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        n = len(nums)
        ans = []

        # put the elements in list as keys and their frequency as values
        for num in nums:
            counter[num] += 1

        res = [[] for i in range(n + 1)]

        # put the elments in an index which is equal to the element's frequency
        for key, value in counter.items():
            res[value].append(key)
        
        for i in range(n, -1, -1):
            if res[i]:
                ans.extend(res[i])
                if len(ans) == k:
                    return ans
            





        


        

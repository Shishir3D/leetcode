class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = defaultdict(list)

        for index, strr in enumerate(strs):
            sorted_str = "".join(sorted(strr))     
            mp[sorted_str].append(index)

        for values in mp.values():
            ans = []
            for i in values:
                ans.append(strs[i])
            res.append(ans)
        
        return res


        

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #store sorted elements as keys and list of elements as values
        #{'aet' : ['ate', 'eat', 'tea']}
        mp_group = defaultdict(list)

        for strr in strs:
            mp_group[str(sorted(strr))].append(strr)
        
        return mp_group.values()






        

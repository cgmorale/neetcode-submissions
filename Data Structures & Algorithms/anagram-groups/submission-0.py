class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for ind_str in strs:
            letters = [0]*26
            for c in ind_str:
                idx = ord(c) - ord("a")
                letters[idx] +=1
            
            groups[tuple(letters)].append(ind_str)
            vals = list(groups.values())
        return vals
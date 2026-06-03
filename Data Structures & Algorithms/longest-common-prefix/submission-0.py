class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        string = strs[0]
        for i in range(len(string)):
            for ind_str in strs:
                if i == len(ind_str) or ind_str[i] != string[i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

            

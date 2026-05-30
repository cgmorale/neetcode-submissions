class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = {}
        dic_t = {}

        for i in range(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = 1
            else: 
                dic_s[s[i]] +=1
            if t[i] not in dic_t:
                dic_t[t[i]] = 1
            else:
                dic_t[t[i]]+=1
        
        return (dic_s == dic_t)


class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for i in s:
            if i in mapping:
                if not check or check[-1] != mapping[i]:
                    return False
                check.pop()
            else:
                check.append(i)
        return not check

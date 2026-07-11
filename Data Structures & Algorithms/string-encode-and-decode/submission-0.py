class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for i in strs:
            newStr = newStr + str(len(i)) + "," + i
        return newStr

    def decode(self, s: str) -> List[str]:
        num = ""
        listOfStrs = []
        i = 0
        while i < len(s):
            comma_index = s.find(",", i)
            num = s[i:comma_index]
            number = int(num)
            word = s[comma_index + 1 : comma_index + 1 + number]
            listOfStrs.append(word)
            i = comma_index + 1 + number
        return listOfStrs
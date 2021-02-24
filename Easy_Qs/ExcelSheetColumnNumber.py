def charValue(char):
    return int(ord(char) - 65 + 1)

class Solution:
    def titleToNumber(self, s: str) -> int:
        rowNumber = 0
        charList = s.split()
        char = len(s)-1
        j = 0
        while(char >=0):
            rowNumber += (charValue(s[char])) * (26**j)
            j += 1
            char -= 1
        return rowNumber
        
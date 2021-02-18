class Solution:
    def romanToInt(self, s: str) -> int:
        mapDict = {'I':1, 'V':5, 'X':10, 
                   'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        ele = 0
        while(ele < len(s)-1):
            curNum = mapDict[s[ele]]                
            if curNum < mapDict[s[ele+1]]:
                curNum = mapDict[s[ele+1]] - curNum
                ele += 1
            num = num + curNum
            ele += 1

        if (ele == len(s)-1):
            if (len(s)==1):
                # single element
                num = num + mapDict[s[ele]]
                return num
            if (s[-1] == s[-2] or mapDict[s[-1]] < mapDict[s[-2]]):
                # handle inputs like III and CCCI
                num = num + mapDict[s[-1]]
                return num
        return num

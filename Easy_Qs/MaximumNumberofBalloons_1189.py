# Input: text = "loonbalxballpoon"
# Output: 2

# Input: text = "leetcode"
# Output: 0

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        QMap = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        QMap.update({'b':text.count('b')})
        QMap.update({'a':text.count('a')})
        QMap.update({'l':text.count('l')})            
        QMap.update({'o':text.count('o')})            
        QMap.update({'n':text.count('n')})        
        print(QMap)
        minNum = min(QMap.values())
        if QMap['l'] >= 2*minNum and QMap['o'] >= 2*minNum:
            return minNum
        minLO = min([QMap['l'], QMap['o']]) 
        return int(minLO/2)
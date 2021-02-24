class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        S = s.split(" ")  # generic split will help, no need to specify the space.
        for se in range(len(S)-1, -1, -1):
            print(S[se])
            if S[se] != u'':
                return len(S[se])            
        return 0
        
# ======================================		
## Optimised solution

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = s.split()
        #print(s_list)
        if len(s_list) == 0:
            return 0
        return len(s_list[-1])		
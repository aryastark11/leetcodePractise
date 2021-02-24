class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n%4 != 0)

    
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <4:
            return True
        if n%4 !=0:
            return True
        return False
     
        
            
        
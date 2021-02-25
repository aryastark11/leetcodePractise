import math
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # has other factors other than 2,3,5
        if num<= 0:
            return False
        while(num>1):
            if num%2 == 0:
                num = num/2
            elif num%3 ==0:
                num = num/3
            elif num%5 == 0:
                num = num/5
            elif num >1:
                return False
        return True
            
# ===========================================

# use while loop to eliminate all 2s, 3s and 5s.
# if n ==1, return True, meaning n is completely divisible by 2,3,5 only
# else return False

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        elif num==1:
            return True
        elif (num%2==0 or num%3==0 or num%5==0):
            
            while num % 2 == 0:
                num /= 2
            while num % 3 == 0:
                num /= 3
            while num % 5 == 0:
                num /= 5
            return num == 1
        else:
            return False            
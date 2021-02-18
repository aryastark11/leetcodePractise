class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if x==0 or +ve number and then compare
        # the reverse and original number
        return True if x>=0 and x == int(str(x)[::-1]) else False
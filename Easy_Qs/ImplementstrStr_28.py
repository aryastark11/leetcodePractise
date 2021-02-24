class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not len(needle):
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)
		
# ==================================================
# optimized solution

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        elif needle not in haystack:
            return -1
        
        else:            
            for (index, character) in enumerate(haystack):
                if character == needle[0]:
                    if haystack[index : index + len(needle)] == needle:
                        return index		
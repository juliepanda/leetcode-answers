# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        nLen = len(needle)
        hLen = len(haystack)
        # defense
        if nLen > hLen:
            return -1
        elif nLen == 0 and hLen == 0:
            return 0
        
        # offense
        for i in range(hLen):
            if haystack[i:i+nLen] == needle:
                return i
        return -1
                

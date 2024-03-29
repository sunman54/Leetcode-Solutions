class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        
        for i,j in enumerate(haystack):
            
            if j == needle[0] and haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
                
                    
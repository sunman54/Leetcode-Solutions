class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        
        prefix = ""
        n = 0
        while True:
            try:
                alf = strs[0][n]
            
                for word in strs:
                    if word[n] != alf:
                        return prefix
                prefix += alf
                n += 1

            except:
                return prefix
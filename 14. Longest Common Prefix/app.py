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
            

        """ best solution
        class Solution:
            def longestCommonPrefix(self, strs: List[str]) -> str:
                for i in range(len(strs[0])):
                    c = strs[0][i]
                    print(c)
                    for s in strs[1:]:
                        if len(s) == i or s[i] != c:
                            return strs[0][0:i]
                return strs[0]
        
        """
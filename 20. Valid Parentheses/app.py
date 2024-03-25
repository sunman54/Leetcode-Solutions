class Solution:
    def isValid(self, s: str) -> bool:

        ph = {'{' : '}', '[' : ']', '(' : ')'}

        to_close = []

        if len(s) %2 == 1:
            return False

        for i in s:

            if i in ph.keys():
                to_close.append(i)

            else:

                if len(to_close) and i == ph.get(to_close[-1]):
                    to_close.pop()
                
                else:
                    return False
        
        if len(to_close) == 0:
            return True
         

        
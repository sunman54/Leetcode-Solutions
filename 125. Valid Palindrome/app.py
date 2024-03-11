class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        x = ''
        
        for i in s :

            if i.isalnum():
                x += i.lower()

        y = x[::-1]

        if x == y : return True
        else: return False

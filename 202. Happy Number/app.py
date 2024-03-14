class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        # Döngüde tekrar eden değerleri takip etmek için bir küme kullanalım
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            # Her adımda n değerini hesaplayalım
            next_n = 0
            for digit in str(n):
                next_n += int(digit) ** 2
            n = next_n

        return n == 1

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
        }
        roman = s
        number = 0

        while len(roman) > 0:

            if  len(roman) < 2:
                number += values.get(roman[0])
                roman = roman[1:]

            elif values.get(roman[0]) >= values.get(roman[1]):
                number += values.get(roman[0])
                roman = roman[1:]

            else: 
                number += values.get(roman[1]) - values.get(roman[0])
                roman = roman[2:]

        return number
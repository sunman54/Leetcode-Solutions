class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        # converting int to binary string
        x = "{0:b}".format(n)

        for i in x:
            if i == '1': 
                result += 1

        return result 
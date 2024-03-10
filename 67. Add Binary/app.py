class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Pad the shorter string with zeros
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        a = a[::-1]
        b = b[::-1]

        result = ''
        carry = 0

        for i in range(max_len):
            # Sum of current bits and carry
            total = int(a[i]) + int(b[i]) + carry

            # Append the sum modulo 2 to result
            result += str(total % 2)

            # Update the carry for the next iteration
            carry = total // 2

        # If there's still a carry after the loop, add it to the result
        if carry:
            result += str(carry)

        # Reverse the result and return
        return result[::-1]
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        single = []

        for i in nums :
            if i in single:
                single.remove(i)

            else:
                single.append(i)

        return single[0]
    
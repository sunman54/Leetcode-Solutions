class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash = {}

        for i,j in enumerate(nums) :


            if j in hash.keys() and abs(i - hash.get(j)) <= k:

                return True


            hash[j] = i


        return False

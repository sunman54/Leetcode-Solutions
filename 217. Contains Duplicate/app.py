class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        map = {}

        for i in (nums):
            if map.get(i) == True:
                return True
            map[i] = True
        
        return False

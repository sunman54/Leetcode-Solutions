class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        for i in range(len(numbers)):
            left = target - numbers[i]
            numbers[i] = 0.1
            
            if left in numbers:
                return [i+1,numbers.index(left)+1]

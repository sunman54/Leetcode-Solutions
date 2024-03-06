class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        d = 1
        res = 0

        for i in digits[::-1] :
            res += i *d
            d *=10

        res +=1

        result = str(res)
        result_list = [] 


        for i in result:
            result_list.append(int(i))


        return result_list

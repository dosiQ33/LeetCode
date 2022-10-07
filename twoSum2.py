class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = 0
        l = len(numbers) -1 
        while (numbers[r]+numbers[l]) != target:
            if (numbers[r]+numbers[l]) > target:
                l-=1
            elif (numbers[r]+numbers[l]) < target:
                r+=1
        return([r+1,l+1])

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = nums.count(0)
        while c != 0:
            nums.remove(0)
            nums.append(0)
            nums[:] = nums
            c-=1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = -1
        for i in range(len(s)//2):
            temp = s[l]
            s[l] = s[i]
            s[i] = temp
            l-=1
        s[:] = s

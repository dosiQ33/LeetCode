class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            longestlen = 0
        else:
            longestlen = 1
        for i in range(len(s)):
            ts = []
            ts.append(s[i])
            for j in range(i+1,len(s)):
                if (s[j] not in ts):
                    ts.append(s[j])
                    if len(ts) > longestlen:
                        longestlen = len(ts)
                else:
                    break
        return(longestlen)

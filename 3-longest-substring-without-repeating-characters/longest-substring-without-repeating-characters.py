class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        m = {}

        for r in range(0,len(s)):
            if s[r] not in m or m[s[r]] < l: #m[s[r]] < l means that the last instance of s[r] was seen outside of the window, meaning this is a unique character again
                m[s[r]] = r
                print(m)
                maxLength = max(maxLength, r-l+1)
            else:
                l=m[s[r]]+1
                m[s[r]]=r
        return maxLength
                




            


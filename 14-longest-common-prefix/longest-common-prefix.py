class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        short = min(strs, key = len)

        for i,ch in enumerate(short):
            for others in strs:
                if others[i]!= ch:
                    return ans
            ans+=others[i]
        return ans


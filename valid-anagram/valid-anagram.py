class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t): return False
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0)+1
            d[t[i]] = d.get(t[i],0)-1
        for i in d.values():
            if i != 0:
                return False
        return True





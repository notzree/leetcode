class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palindrome = []
        def dfs(i):
            if i>=len(s):
                res.append(palindrome.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s,i,j):
                    palindrome.append(s[i:j+1])
                    dfs(j+1)
                    palindrome.pop()
        dfs(0)
        return res

    def isPali(self, s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        return True


        
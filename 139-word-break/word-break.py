class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sLength = len(s)
        memo = {}
        def dfs(left):
            if left >= sLength:
                return True
            for right in range(left, sLength):
                if (left,right+1) in memo:
                    return memo[(left,right+1)]
                if s[left:right+1] in wordDict :
                    #branch by setting left pointer to the right pointer+1
                    if dfs(right+1):
                        return True
                    else:
                        memo[(left,right+1)] = False
            return False
        return dfs(0)
            

        
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def dfs(i): #position that we are at
            if i in dp: #Either last position or alr cached
                print(dp)
                return dp[i]
            if s[i]=="0":
                return 0
            #Take i as a single digit
            res = dfs(i+1)
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and int(s[i+1])<=6)):
                res+= dfs(i+2)
            dp[i] = res
            print(dp)
            return res
        return dfs(0)
        


            




        
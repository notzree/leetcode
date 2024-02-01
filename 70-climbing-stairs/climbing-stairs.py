class Solution:
    def climbStairs(self, n: int) -> int:
        #Return the number of ways one can climb to the top
        if n == 1:
            return 1
        if n==2:
            return 2
        dp = [-1]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            print(dp[i])
        return dp[n]

        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0: return 0
        if len(coins) ==1:
            return amount//coins[0] if (amount%coins[0] == 0) else -1
        dp={}
        for c in coins: #populate DP array with info we already know
            dp[c]=1

        def dfs(t):
            if t == 0:
                return 0
            if t in dp:
                return dp[t]
            short = float("inf")
            for c in coins:
                if c <=t:
                    short = min(short,dfs(t-c)+1)
            dp[t] = short
            return dp[t]

        res = dfs(amount)
        return res if res != float("inf") else -1



        
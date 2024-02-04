class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount ==0: return 0
        # if len(coins) ==1:
        #     return amount//coins[0] if (amount%coins[0] == 0) else -1
        # dp={}
        # for c in coins: #populate DP array with info we already know
        #     dp[c]=1
        # def dfs(t):
        #     if t == 0:
        #         return 0
        #     if t in dp:
        #         return dp[t]
        #     short = float("inf")
        #     for c in coins:
        #         if c <=t:
        #             short = min(short,dfs(t-c)+1)
        #     dp[t] = short
        #     return dp[t]
        # res = dfs(amount)
        # return res if res != float("inf") else -1

        dp=[amount+1] * (amount+1)
        dp[0] = 0
        for t in range(1,amount+1):
            for c in coins:
                if c <=t: #Ensure we don't go go over the sum
                    dp[t] = min(dp[t-c] + 1, dp[t]) #1 conmes from the current coin we are using

        return dp[amount] if dp[amount] != amount+1 else -1
        
                

            




        
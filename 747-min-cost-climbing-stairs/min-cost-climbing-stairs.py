class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <=2:
            return min(cost[0], cost[1])
        prev_one = cost[1] # starting from 1
        prev_two = cost[0] # starting from 0
        for i in range(2,len(cost)):
            prev_one, prev_two = min(prev_one, prev_two) + cost[i], prev_one
        return min(prev_one, prev_two)


        
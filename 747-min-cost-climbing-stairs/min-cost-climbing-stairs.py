class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <=2:
            return min(cost[0], cost[1])
        prev_one = cost[1] # starting from 1
        prev_two = cost[0] # starting from 0
        for i in range(2,len(cost)):
            current_cost = min(prev_one, prev_two) + cost[i]
            prev_two = prev_one
            prev_one = current_cost
        return min(prev_one, prev_two)


        
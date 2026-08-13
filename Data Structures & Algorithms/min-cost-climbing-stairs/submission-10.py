class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom down approach I guess
        n = len(cost) 
        Total_cost = [0]*n 
        Total_cost[n-1] = cost[n-1]
        Total_cost[n-2] = cost[n-2]
        mock_list= []
        for i in range(3, n+1):
            if Total_cost[n-i+1] > Total_cost[n-i+2]:
                Total_cost[n-i] = cost[n-i] + Total_cost[n-i+2]
            else:
                Total_cost[n-i] = cost[n-i] + Total_cost[n-i +1]
        if Total_cost[0] < Total_cost[1]:
            return Total_cost[0]
        else: 
            return Total_cost[1]
    

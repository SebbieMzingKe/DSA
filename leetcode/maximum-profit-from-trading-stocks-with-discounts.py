class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """

        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u - 1].append(v - 1)

        def merge(dp1, dp2):
            new_dp = [-float('inf')] * (budget + 1)

            for c1 in range(budget + 1):
                if dp1[c1] == -float('inf'): continue

                for c2 in range(budget - c1 + 1):
                    if dp2[c2] == -float('inf'): continue

                    if dp1[c1] + dp2[c2] > new_dp[c1 + c2]:
                        new_dp[c1 + c2] = dp1[c1] + dp2[c2]

            return new_dp

        
        def dfs(u):
            agg_with_buy = [-float('inf')] * (budget + 1)
            agg_with_buy[0] = 0

            agg_with_skip = [-float('inf')] * (budget + 1)
            agg_with_skip[0] = 0

            for v in adj[u]:
                child_res_parent_bought, child_res_parent_skipped = dfs(v)

                agg_with_buy = merge(agg_with_buy, child_res_parent_bought)

                agg_with_skip = merge(agg_with_skip, child_res_parent_skipped)

            res_parent_bought = [-float('inf')] * (budget + 1)
            res_parent_skipped = [-float('inf')] * (budget + 1)

            cost_full = present[u]
            profit_full = future[u] - present[u]

            cost_discount = present[u] // 2
            profit_discount = future[u] - cost_discount


            for c in range(budget - cost_full + 1):
                if agg_with_buy[c] != -float('inf'):
                    res_parent_skipped[c + cost_full] = max(res_parent_skipped[c + cost_full], agg_with_buy[c] + profit_full)


            for c in range(budget + 1):
                if agg_with_skip[c] != -float('inf'):
                    res_parent_skipped[c] = max(res_parent_skipped[c], agg_with_skip[c])
          
            for c in range(budget - cost_discount + 1):
                if agg_with_buy[c] != -float('inf'):
                    res_parent_bought[c + cost_discount] = max(res_parent_bought[c + cost_discount], agg_with_buy[c] + profit_discount)


            for c in range(budget + 1):
                if agg_with_skip[c] != -float('inf'):
                    res_parent_bought[c] = max(res_parent_bought[c], agg_with_skip[c])
            
            return res_parent_bought, res_parent_skipped

        _, final_dp = dfs(0)
        return max(0, max(final_dp))

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    # Employee 1 buys (cost 1, profit 3). Employee 2 buys (cost 1 [discounted], profit 2).
    # Total Cost 2, Total Profit 5.
    print(f"Test Case 1: {solver.maxProfit(2, [1,2], [4,3], [[1,2]], 3)} (Expected: 5)")

    # Test Case 2
    # Budget 4. Buying both costs 3+2=5 (too much) or 3+4=7 (too much).
    # Can only buy one. Employee 2 profit is 8-4=4. Employee 1 profit is 5-3=2. Max is 4.
    print(f"Test Case 2: {solver.maxProfit(2, [3,4], [5,8], [[1,2]], 4)} (Expected: 4)")

    # Test Case 3
    # 1 buys (4->7, prof 3). 3 buys discounted (4->11, prof 7). Total cost 4+4=8. Profit 10.
    print(f"Test Case 3: {solver.maxProfit(3, [4,6,8], [7,9,11], [[1,2],[1,3]], 10)} (Expected: 10)")

    # Test Case 4
    # All buy. 1 buys (5->8, prof 3). 2 buys discounted (1->5, prof 4). 3 buys discounted (1->6, prof 5).
    # Total Cost: 5 + 1 + 1 = 7. Total Profit: 3 + 4 + 5 = 12.
    print(f"Test Case 4: {solver.maxProfit(3, [5,2,3], [8,5,6], [[1,2],[2,3]], 7)} (Expected: 12)")
class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        
        # dp[i][j]: min cost to fix first i robots with first j factories
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        
        # Base case: 0 robots cost = 0
        for j in range(m + 1):
            dp[0][j] = 0
        
        for j in range(1, m + 1):
            pos, limit = factory[j - 1]
            
            for i in range(1, n + 1):
                # Option 1: skip this factory
                dp[i][j] = dp[i][j - 1]
                
                # Option 2: assign k robots to this factory
                dist = 0
                for k in range(1, min(limit, i) + 1):
                    dist += abs(robot[i - k] - pos)
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - k][j - 1] + dist
                    )
        
        return dp[n][m] 

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, robot, factory, expected):
        result = solver.minimumTotalDistance(robot, factory)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Robots:   {robot}")
        print(f"  Factory:  {factory}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [0, 4, 6], [[2, 2], [6, 2]], 4)

    # Example 2
    run_test(2, [1, -1], [[-2, 1], [2, 1]], 2)
    
    # Custom Case 3: More factory slots than needed
    run_test(3, [1, 2, 3], [[10, 5]], 24) # 1->10 (9), 2->10 (8), 3->10 (7) = 24
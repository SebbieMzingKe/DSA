class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        slots = []
        for pos, limit in factory:
            for _ in range(limit):
                slots.append(pos)
                
        n, m = len(robot), len(slots)
        memo = {}
        
        def dp(i, j):
            if i == n: return 0
            if j == m: return float('inf')
            if (i, j) in memo: return memo[(i, j)]
            
            assign = abs(robot[i] - slots[j]) + dp(i + 1, j + 1)
            skip = dp(i, j + 1)
            
            ans = min(assign, skip)
            memo[(i, j)] = ans
            return ans
            
        return dp(0, 0)

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
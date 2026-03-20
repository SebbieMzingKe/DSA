class Solution(object):
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])

        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                distinct_vals = set()

                for r in range(i, i + k):
                    for c in range(j, j + k):
                        distinct_vals.add(grid[r][c])
                
                if len(distinct_vals) <= 1:
                    ans[i][j] = 0
                
                else:
                    sorted_vals = sorted(list(distinct_vals))
                    min_diff = float('inf')

                    for v in range(1, len(sorted_vals)):
                        min_diff = min(min_diff, sorted_vals[v] - sorted_vals[v - 1])
                    
                    ans[i][j] =min_diff
        
        return ans

if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, grid, k, expected):
        result = solver.minAbsDiff(grid, k)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}: k={k}")
        print("  Grid:")
        for row in grid:
            print(f"    {row}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [[1, 8], [3, -2]], 2, [[2]])

    # Example 2
    run_test(2, [[3, -1]], 1, [[0, 0]])

    # Example 3
    run_test(3, [[1, -2, 3], [2, 3, 5]], 2, [[1, 2]])

    # Custom Case: All same elements
    run_test(4, [[5, 5], [5, 5]], 2, [[0]])

    # Custom Case: Larger grid
    run_test(5, [[1, 5, 9], [2, 6, 10], [3, 7, 11]], 2, [[1, 1], [1, 1]])

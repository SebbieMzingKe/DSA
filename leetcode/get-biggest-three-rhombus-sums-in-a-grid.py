class Solution(object):
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        distinct_sums = set()

        for i in range(m):
            for j in range(n):
                distinct_sums.add(grid[i][j])

                L = 1

                while i + 2 * L < m and j - L >= 0 and j + L < n:
                    current_sum = 0

                    for k in range(L):
                        current_sum += grid[i + k][j + k]
                    for k in range(L):
                        current_sum += grid[i + L + k][j + L - k]
                    for k in range(L):
                        current_sum += grid[i + 2 * L - k][j - k]
                    for k in range(L):
                        current_sum += grid[i + L - k][j - L + k]
                    
                    distinct_sums.add(current_sum)
                    L += 1
        
        return sorted(list(distinct_sums), reverse = True)[:3]
    
if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, grid, expected):
        result = solver.getBiggestThree(grid)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}:")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    grid1 = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
    run_test(1, grid1, [228, 216, 211])

    # Example 2
    grid2 = [[1,2,3],[4,5,6],[7,8,9]]
    run_test(2, grid2, [20, 9, 8])

    # Example 3
    grid3 = [[7,7,7]]
    run_test(3, grid3, [7])
    
    # Custom Case: Single cell grid
    run_test(4, [[100]], [100])
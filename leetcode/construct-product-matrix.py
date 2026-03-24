class Solution(object):
    def constructProductMatrix(self, grid):
        n = len(grid)
        m = len(grid[0])
        MOD = 12345

        p = [[1] * m for _ in range(n)]

        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD

        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD
        
        return p

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, grid, expected):
        result = solver.constructProductMatrix(grid)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print("  Grid:")
        for row in grid:
            print(f"    {row}")
        print("  Output:")
        for row in result:
            print(f"    {row}")
        print(f"  Expected:")
        for row in expected:
            print(f"    {row}")
        print(f"  Status: {status}\n")

    # Example 1
    run_test(1, [[1,2],[3,4]], [[24,12],[8,6]])

    # Example 2
    # 12345 % 12345 is 0, so any product containing it will be 0 (except its own spot)
    run_test(2, [[12345],[2],[1]], [[2],[0],[0]])

    # Custom Case: Contains a zero
    run_test(3, [[1, 2], [0, 4]], [[0, 0], [8, 0]])
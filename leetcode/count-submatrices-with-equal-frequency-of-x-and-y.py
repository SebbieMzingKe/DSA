class Solution(object):
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        col_bal  = [0] * n
        col_x = [0] * n
        valid_submatrices = 0

        for i in range(m):
            curr_submatrix_bal = 0
            curr_submatrix_x = 0

            for j in range(n):
                char = grid[i][j]
                
                if char == 'X':
                    col_bal[j] += 1
                    col_x[j] += 1
                
                elif char == 'Y':
                    col_bal[j] -= 1

                curr_submatrix_bal += col_bal[j]
                curr_submatrix_x += col_x[j]

                if curr_submatrix_bal == 0 and curr_submatrix_x > 0:
                    valid_submatrices += 1
            
        return valid_submatrices

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, grid, expected):
        result = solver.numberOfSubmatrices(grid)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        for row in grid:
            print(f"  {row}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"Status:   {status}\n")

    # Example 1
    run_test(1, [["X","Y","."],["Y",".","."]], 3)

    # Example 2
    run_test(2, [["X","X"],["X","Y"]], 0)

    # Example 3
    run_test(3, [[".","."],[".","."]], 0)
    
    # Custom Case: Single cell X
    run_test(4, [["X"]], 0)
    
    # Custom Case: Balanced row
    run_test(5, [["X", "Y", "X", "Y"]], 2)
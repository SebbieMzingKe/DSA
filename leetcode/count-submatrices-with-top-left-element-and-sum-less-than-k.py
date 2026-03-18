class Solution(object):
    def countSubmatrices(self, grid, k):
        m, n = len(grid), len(grid[0])
        col_sums = [0] * n
        current_cols = n
        count = 0

        for i in range(m):
            row_sum = 0
            for j in range(current_cols):
                row_sum += grid[i][j]
                col_sums[j] += row_sum

                if col_sums[j] <= k:
                    count += 1
                else:
                    current_cols = j
                    break

        return count


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, grid, k, expected):
        result = solver.countSubmatrices(grid, k)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}: k={k}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [[7, 6, 3], [6, 6, 1]], 18, 4)

    # Example 2
    run_test(2, [[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20, 6)

    # Custom Case: All elements are larger than k
    run_test(3, [[10, 10], [10, 10]], 5, 0)

    # Custom Case: Single element grid
    run_test(4, [[5]], 10, 1)

    # Custom Case: Large grid with early cutoff
    grid_large = [[1, 1, 1, 100], [1, 1, 1, 1], [1, 1, 1, 1]]
    run_test(5, grid_large, 10, 9)

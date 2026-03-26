from collections import Counter


class Solution(object):
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])

        if m > 1:
            bot_counts = Counter()
            for i in range(m):
                for j in range(n):
                    bot_counts[grid[i][j]] += 1
            top_counts = Counter()
            sum_top = 0
            sum_bot = sum(k * v for k, v in bot_counts.items())

            for i in range(m - 1):
                for j in range(n):
                    v = grid[i][j]
                    top_counts[v] += 1
                    sum_top += v
                    bot_counts[v] -= 1
                    sum_bot -= v
                    if bot_counts[v] == 0:
                        del bot_counts[v]
                diff = sum_top - sum_bot
                if diff == 0:
                    return True
                elif diff > 0:
                    if i == 0:
                        if grid[0][0] == diff or grid[0][n - 1] == diff:
                            return True
                    elif n == 1:
                        if grid[0][0] == diff or grid[i][0] == diff:
                            return True
                    else:
                        if diff in top_counts:
                            return True
                else:
                    target = -diff
                    if i == m - 2:
                        if grid[m - 1][0] == target or grid[m - 1][n - 1] == target:
                            return True
                    elif n == 1:
                        if grid[i + 1][0] == target or grid[m - 1][0] == target:
                            return True
                    else:
                        if target in bot_counts:
                            return True

        if n > 1:
            right_counts = Counter()
            for i in range(m):
                for j in range(n):
                    right_counts[grid[i][j]] += 1
            left_counts = Counter()
            sum_left = 0
            sum_right = sum(k * v for k, v in right_counts.items())

            for j in range(n - 1):
                for i in range(m):
                    v = grid[i][j]
                    left_counts[v] += 1
                    sum_left += v
                    right_counts[v] -= 1
                    sum_right -= v
                    if right_counts[v] == 0:
                        del right_counts[v]
                diff = sum_left - sum_right
                if diff == 0:
                    return True
                elif diff > 0:
                    if j == 0:
                        if grid[0][0] == diff or grid[m - 1][0] == diff:
                            return True
                    elif m == 1:
                        if grid[0][0] == diff or grid[0][j] == diff:
                            return True
                    else:
                        if diff in left_counts:
                            return True
                else:
                    target = -diff
                    if j == n - 2:
                        if grid[0][n - 1] == target or grid[m - 1][n - 1] == target:
                            return True
                    elif m == 1:
                        if grid[0][j + 1] == target or grid[0][n - 1] == target:
                            return True
                    else:
                        if target in right_counts:
                            return True

        return False


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, grid, expected):
        result = solver.canPartitionGrid(grid)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print("  Grid:")
        for row in grid:
            print(f"    {row}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [[1, 4], [2, 3]], True)

    # Example 2
    run_test(2, [[1, 2], [3, 4]], True)

    # Example 3 (Disconnects bottom)
    run_test(3, [[1, 2, 4], [2, 3, 5]], False)

    # Example 4
    run_test(4, [[4, 1, 8], [3, 2, 6]], False)

    # Custom Case: 1D Array where end removal works
    run_test(5, [[5, 2, 3]], True)

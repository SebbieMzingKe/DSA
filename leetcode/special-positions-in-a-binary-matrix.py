class Solution(object):
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        row_counts = [0] * m
        col_counts = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1

        special_count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_counts[i] == 1 and col_counts[j] == 1:
                    special_count += 1

        return special_count


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, mat, expected):
        result = solver.numSpecial(mat)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        for row in mat:
            print(f"  {row}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"Status:   {status}\n")

    # Example 1
    # row counts: [1, 1, 1]
    # col counts: [2, 0, 1]
    # Special at (1, 2)
    run_test(1, [[1, 0, 0], [0, 0, 1], [1, 0, 0]], 1)

    # Example 2
    # Identity matrix. All three 1s are special.
    run_test(2, [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)

    # Custom Case: No special positions
    # row counts: [2, 2]
    # col counts: [2, 2]
    run_test(3, [[1, 1], [1, 1]], 0)

    # Custom Case: Rectangular matrix
    run_test(4, [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 2)

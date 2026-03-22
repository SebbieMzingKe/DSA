class Solution(object):
    def findRotation(self, mat, target):
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(row) for row in zip(*mat[::-1])]
        return False


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, mat, target, expected):
        result = solver.findRotation(mat, target)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    # Rotate 90 degrees once to match
    run_test(1, [[0, 1], [1, 0]], [[1, 0], [0, 1]], True)

    # Example 2
    # Impossible to match (number of 1s and 0s are different)
    run_test(2, [[0, 1], [1, 1]], [[1, 0], [0, 1]], False)

    # Example 3
    # Rotate 180 degrees to match
    run_test(
        3, [[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]], True
    )

    # Custom Case: 0 degree rotation (already matches)
    run_test(4, [[1, 0], [0, 1]], [[1, 0], [0, 1]], True)

    # Custom Case: 3x3 matrix rotated 270 degrees
    mat5 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    target5 = [[2, 5, 8], [1, 4, 7], [0, 3, 6]]
    run_test(5, mat5, target5, True)

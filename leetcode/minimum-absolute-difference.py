class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()

        min_diff = float("inf")
        result = []

        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]

            if diff < min_diff:
                min_diff = diff

                result = [[arr[i], arr[i + 1]]]

            elif diff == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, arr, expected):
        result = solver.minimumAbsDifference(list(arr))
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: {arr} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # Sorted: [1, 2, 3, 4]. Min diff is 1. Pairs: [1,2], [2,3], [3,4]
    run_test(1, [4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]])

    # Example 2
    # Sorted: [1, 3, 6, 10, 15]. Diffs: 2, 3, 4, 5. Min is 2.
    run_test(2, [1, 3, 6, 10, 15], [[1, 3]])

    # Example 3 (Negative numbers)
    # Sorted: [-14, -10, -4, 3, 8, 19, 23, 27]
    # Diffs: 4, 6, 7, 5, 11, 4, 4. Min is 4.
    # Pairs: [-14, -10], [19, 23], [23, 27]
    run_test(3, [3, 8, -10, 23, 19, -4, -14, 27], [[-14, -10], [19, 23], [23, 27]])

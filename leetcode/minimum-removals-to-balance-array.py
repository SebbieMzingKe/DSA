class Solution(object):
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)

        max_kept = 0
        left = 0

        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1

            current_window_size = right - left + 1

            if current_window_size > max_kept:

                max_kept = current_window_size

        return n - max_kept


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, k, expected):
        result = solver.minRemoval(list(nums), k)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: {nums}, k={k} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # Sort: [1, 2, 5]. k=2.
    # Window [1, 2]: 2 <= 1*2 (Valid). Len 2.
    # Window [2, 5]: 5 <= 2*2 (Invalid).
    # Max kept 2. Removals: 3 - 2 = 1.
    run_test(1, [2, 1, 5], 2, 1)

    # Example 2
    # Sort: [1, 2, 6, 9]. k=3.
    # [1, 2]: 2<=3. OK.
    # [1...6]: 6 > 1*3. Invalid. Left moves.
    # [2, 6]: 6 <= 2*3. OK. Len 2.
    # [6, 9]: 9 <= 6*3. OK. Len 2.
    # Max kept 2. Removals: 4 - 2 = 2.
    run_test(2, [1, 6, 2, 9], 3, 2)

    # Example 3
    # Sort: [4, 6]. k=2. 6 <= 4*2 (8). Valid.
    # Removals: 0.
    run_test(3, [4, 6], 2, 0)

    # Custom Case: All same
    # [5,5,5], k=1. 5 <= 5*1. Valid. 0 removals.
    run_test(4, [5, 5, 5], 1, 0)

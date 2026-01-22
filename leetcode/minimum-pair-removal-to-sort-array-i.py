class Solution(object):
    def minimumPairRemoval(self, nums):
        operations = 0

        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False

            return True

        current_nums = list(nums)

        while not is_sorted(current_nums):
            min_sum = float("inf")
            target_index = -1

            for i in range(len(current_nums) - 1):
                s = current_nums[i] + current_nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    target_index = i

            new_val = current_nums[target_index] + current_nums[target_index + 1]

            current_nums = (
                current_nums[:target_index]
                + [new_val]
                + current_nums[target_index + 2 :]
            )
            operations += 1

        return operations


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.minimumPairRemoval(nums)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: Input {nums} -> Output {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # [5,2,3,1] -> Pair (3,1) sum 4 (min). New: [5,2,4]
    # [5,2,4]   -> Pair (2,4) sum 6 (min). New: [5,6] (Sorted)
    # Total ops: 2
    run_test(1, [5, 2, 3, 1], 2)

    # Example 2
    # [1,2,2] -> Already sorted.
    run_test(2, [1, 2, 2], 0)

    # Edge Case: Reverse sorted
    # [3, 2, 1] -> Pair (2,1) sum 3. New: [3, 3] (Sorted)
    # Total ops: 1
    run_test(3, [3, 2, 1], 1)

    # Tie Breaker Case
    # [5, 1, 1, 5]
    # Pairs: (5,1)=6, (1,1)=2, (1,5)=6. Min is 2 at idx 1.
    # New: [5, 2, 5]. Sorted? No.
    # Pairs: (5,2)=7, (2,5)=7. Tie. Pick left (5,2).
    # New: [7, 5]. Sorted? No.
    # Pairs: (7,5)=12. New: [12]. Sorted? Yes.
    # Total ops: 3
    run_test(4, [5, 1, 1, 5], 3)

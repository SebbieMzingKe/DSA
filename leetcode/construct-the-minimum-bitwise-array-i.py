class Solution(object):
    def minBitwiseArray(self, nums):

        ans = []

        for n in nums:
            found = False

            for x in range(n):
                if (x | (x + 1)) == n:
                    ans.append(x)
                    found = True
                    break

            if not found:
                ans.append(-1)

        return ans


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.minBitwiseArray(nums)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: Input {nums} -> Output {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # 2: Even prime, result -1
    # 3: 1 | 2 = 3
    # 5: 4 | 5 = 5
    # 7: 3 | 4 = 7
    run_test(1, [2, 3, 5, 7], [-1, 1, 4, 3])

    # Example 2
    # 11 (1011): x=9 (1001) -> 9|10 = 1011 (11)
    # 13 (1101): x=12 (1100) -> 12|13 = 1101 (13)
    # 31 (11111): x=15 (01111) -> 15|16 = 11111 (31)
    run_test(2, [11, 13, 31], [9, 12, 15])

    # Custom Edge Case
    # Only 2
    run_test(3, [2], [-1])

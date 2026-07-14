from collections import defaultdict
import math


class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        dp = defaultdict(int)
        dp[(0, 0)] = 1

        for x in nums:
            next_dp = defaultdict(int)
            for (g1, g2), count in dp.items():
                next_dp[(g1, g2)] = (next_dp[(g1, g2)] + count) % MOD

                ng1 = math.gcd(g1, x)
                next_dp[(ng1, g2)] = (next_dp[(ng1, g2)] + count) % MOD

                ng2 = math.gcd(g2, x)
                next_dp[(g1, ng2)] = (next_dp[(g1, ng2)] + count) % MOD

            dp = next_dp

        ans = 0
        for g in range(1, 201):
            if (g, g) in dp:
                ans = (ans + dp[(g, g)]) % MOD

        return ans


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.subsequencePairCount(nums)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    nums = {nums}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [1, 2, 3, 4], 10)

    # Example 2
    run_test(2, [10, 20, 30], 2)

    # Example 3
    run_test(3, [1, 1, 1, 1], 50)

    # Custom Case 4: Pair with no common GCDs aside from trivial ones
    run_test(4, [2, 3, 5], 0)

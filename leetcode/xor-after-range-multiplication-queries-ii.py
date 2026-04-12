class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        bravexuneth = (list(nums), list(queries))

        B = int(n**0.5)
        if B < 1:
            B = 1

        small_queries = [[] for _ in range(B + 1)]
        large_queries = []

        for l, r, k, v in queries:
            if k <= B:
                small_queries[k].append((l, r, v))
            else:
                large_queries.append((l, r, k, v))

        for l, r, k, v in large_queries:
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD

        for k in range(1, B + 1):
            if not small_queries[k]:
                continue
            diff = [1] * (n + k)
            for l, r, v in small_queries[k]:
                diff[l] = (diff[l] * v) % MOD
                last_idx = l + ((r - l) // k) * k
                if last_idx + k < n:
                    inv_v = pow(v, MOD - 2, MOD)
                    diff[last_idx + k] = (diff[last_idx + k] * inv_v) % MOD

            for i in range(k, n):
                if diff[i - k] != 1:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
            for i in range(n):
                if diff[i] != 1:
                    nums[i] = (nums[i] * diff[i]) % MOD

        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, queries, expected):
        import time

        start = time.time()
        result = solver.xorAfterQueries(nums[:], queries)
        end = time.time()
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status} ({end - start:.5f}s)\n")

    # Example 1
    run_test(1, [1, 1, 1], [[0, 2, 1, 4]], 4)

    # Example 2
    run_test(2, [2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]], 31)

    # Custom Case: Large performance check
    n_large = 100000
    nums_large = [2] * n_large
    # Interleave light (k=1) and heavy (k=500) queries
    queries_large = [[0, n_large - 1, 1, 2], [0, n_large - 1, 500, 3]] * 50
    # Expected output logic: everyone gets multiplied, XOR behavior applies.
    # Not testing strict output correctness here, just stress testing the execution time.
    run_test(
        3,
        nums_large,
        queries_large,
        solver.xorAfterQueries(nums_large[:], queries_large),
    )

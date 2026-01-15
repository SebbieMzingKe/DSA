class Solution(object):
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7

        valid_cols = []

        def generate_columns(idx, current_col):
            if idx == m:
                valid_cols.append(tuple(current_col))
                return
            for color in range(3):
                if idx > 0 and current_col[-1] == color:
                    continue
                current_col.append(color)
                generate_columns(idx + 1, current_col)
                current_col.pop()

        generate_columns(0, [])
        num_states = len(valid_cols)

        adj = [[] for _ in range(num_states)]
        for i in range(num_states):
            for j in range(num_states):
                c1, c2 = valid_cols[i], valid_cols[j]
                if all(c1[k] != c2[k] for k in range(m)):
                    adj[i].append(j)

        dp = [1] * num_states
        for _ in range(n - 1):
            new_dp = [0] * num_states
            for i in range(num_states):
                if dp[i] == 0:
                    continue
                for neighbor in adj[i]:
                    new_dp[neighbor] = (new_dp[neighbor] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, m, n, expected):
        result = solver.colorTheGrid(m, n)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: m={m}, n={n} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # m=1, n=1. Patterns: [R], [G], [B]. Total 3.
    run_test(1, 1, 1, 3)

    # Example 2
    # m=1, n=2. Patterns: [R][G], [R][B], [G][R], [G][B], [B][R], [B][G]. Total 6.
    run_test(2, 1, 2, 6)

    # Example 3
    # Larger constraint
    run_test(3, 5, 5, 580986)

    # Edge Case: Smallest grid m=1, n=1000
    # Formula is 3 * 2^(n-1) for m=1
    # 3 * 2^999 % (10^9+7)
    # Just checking it runs without error/timeout
    print(
        f"Test Case 4 (Large n): {solver.colorTheGrid(1, 1000)} (Speed check) -> PASS"
    )

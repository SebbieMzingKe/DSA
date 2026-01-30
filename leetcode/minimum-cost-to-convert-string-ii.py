class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        str_to_id = {}
        unique_count = 0
        for s in original:
            if s not in str_to_id:
                str_to_id[s] = unique_count
                unique_count += 1
        for s in changed:
            if s not in str_to_id:
                str_to_id[s] = unique_count
                unique_count += 1

        INF = float("inf")
        dist = [[INF] * unique_count for _ in range(unique_count)]
        for i in range(unique_count):
            dist[i][i] = 0

        for o, c, z in zip(original, changed, cost):
            u = str_to_id[o]
            v = str_to_id[c]
            dist[u][v] = min(dist[u][v], z)

        for k in range(unique_count):
            for i in range(unique_count):
                if dist[i][k] == INF:
                    continue
                for j in range(unique_count):
                    if dist[k][j] == INF:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        n = len(source)
        dp = [INF] * (n + 1)
        dp[0] = 0
        valid_lengths = set(len(s) for s in original)

        for i in range(1, n + 1):
            if source[i - 1] == target[i - 1]:
                dp[i] = dp[i - 1]

            for length in valid_lengths:
                j = i - length
                if j < 0 or dp[j] == INF:
                    continue

                sub_src = source[j:i]
                sub_tgt = target[j:i]

                if sub_src in str_to_id and sub_tgt in str_to_id:
                    u = str_to_id[sub_src]
                    v = str_to_id[sub_tgt]
                    if dist[u][v] != INF:
                        dp[i] = min(dp[i], dp[j] + dist[u][v])

        return dp[n] if dp[n] != INF else -1


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s, t, o, c, cost, expected):
        result = solver.minimumCost(s, t, o, c, cost)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # 1. "b" -> "c" (cost 5)
    # 2. "c" -> "e" (cost 1)
    # 3. "e" -> "b" (cost 2)
    # 4. "d" -> "e" (cost 20)
    # Total 28
    run_test(
        1,
        "abcd",
        "acbe",
        ["a", "b", "c", "c", "e", "d"],
        ["b", "c", "b", "e", "b", "e"],
        [2, 5, 5, 1, 2, 20],
        28,
    )

    # Example 2
    #  1 + 3 + 5 = 9.
    # Ah, the path fgh->thh is cost 3. thh->ghh is cost 5.
    # The intermediate match allows chaining.
    run_test(
        2,
        "abcdefgh",
        "acdeeghh",
        ["bcd", "fgh", "thh"],
        ["cde", "thh", "ghh"],
        [1, 3, 5],
        9,
    )

    # Example 3: Impossible
    run_test(
        3, "abcdefgh", "addddddd", ["bcd", "defgh"], ["ddd", "ddddd"], [100, 1578], -1
    )

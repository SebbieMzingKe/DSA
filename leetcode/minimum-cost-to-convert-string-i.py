class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = float("inf")
        dist = [[INF] * 26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0

        for o, c, z in zip(original, changed, cost):
            u = ord(o) - ord("a")
            v = ord(c) - ord("a")
            dist[u][v] = min(dist[u][v], z)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        total_cost = 0
        for s_char, t_char in zip(source, target):
            u = ord(s_char) - ord("a")
            v = ord(t_char) - ord("a")
            if dist[u][v] == INF:
                return -1
            total_cost += dist[u][v]

        return total_cost


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, source, target, original, changed, cost, expected):
        result = solver.minimumCost(source, target, original, changed, cost)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1 input: source="abcd", target="acbe"
    # source[0]='a', target[0]='a' -> cost 0
    # source[1]='b', target[1]='c' -> cost 5 (direct)
    # source[2]='c', target[2]='b' -> c->e(1)->b(2) = 3 (via e)
    # source[3]='d', target[3]='e' -> cost 20 (direct)
    # Total: 0 + 5 + 3 + 20 = 28.
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
    # a->b requires a->c(1) + c->b(2) = 3.
    # 4 occurrences of a->b. 4 * 3 = 12.
    run_test(2, "aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2], 12)

    # Example 3
    # d->e impossible.
    run_test(3, "abcd", "abce", ["a"], ["e"], [10000], -1)

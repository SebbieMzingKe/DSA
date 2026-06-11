from collections import defaultdict, deque


class Solution(object):
    def assignEdgeWeights(self, edges):
        if not edges:
            return 0

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(1, 0)])
        visited = {1}
        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for neighbour in adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append((neighbour, depth + 1))

        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, edges, expected):
        result = solver.assignEdgeWeights(edges)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    edges = {edges}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [[1, 2]], 1)

    # Example 2
    run_test(2, [[1, 2], [1, 3], [3, 4], [3, 5]], 2)

    # Custom Case 3: A deep straight line tree 1-2-3-4-5 (max depth 4)
    # 2^(4-1) = 2^3 = 8
    run_test(3, [[1, 2], [2, 3], [3, 4], [4, 5]], 8)

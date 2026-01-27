import heapq


class Solution(object):
    def minCost(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        pq = [(0, 0)]
        min_dist = [float("inf")] * n
        min_dist[0] = 0

        while pq:
            cost, u = heapq.heappop(pq)
            if u == n - 1:
                return cost

            if cost > min_dist[u]:
                continue

            for v, w in graph[u]:
                new_cost = cost + w

                if new_cost < min_dist[v]:
                    min_dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
        return -1


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, edges, expected):
        result = solver.minCost(n, edges)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: Output {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # Path: 0 -> 1 (3), then reverse 3->1 to get 1->3 (2*1=2). Total 5.
    n1 = 4
    edges1 = [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]
    run_test(1, n1, edges1, 5)

    # Example 2
    # Path: 0->2 (1), 2->1 (1), 1->3 (1). Total 3. No reversals needed.
    n2 = 4
    edges2 = [[0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 3]]
    run_test(2, n2, edges2, 3)

    # Example 3: Disconnected
    n3 = 3
    edges3 = [[0, 1, 1]]
    run_test(3, n3, edges3, -1)

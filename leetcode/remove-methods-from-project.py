class Solution(object):
    def remainingMethods(self, n, k, invocations):
        adj = [[] for _ in range(n)]

        for u, v in invocations:
            adj[u].append(v)

        suspicious = [False] * n
        suspicious[k] = True

        stack = [k]

        while stack:
            curr = stack.pop()
            for neighbour in adj[curr]:
                if not suspicious[neighbour]:
                    suspicious[neighbour] = True
                    stack.append(neighbour)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, k, invocations, expected):
        # We sort both lists to ensure the order of the answer doesn't cause a false failure
        result = sorted(solver.remainingMethods(n, k, invocations))
        expected_sorted = sorted(expected)

        status = "PASS" if result == expected_sorted else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    n = {n}, k = {k}, invocations = {invocations}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected_sorted}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, 4, 1, [[1, 2], [0, 1], [3, 2]], [0, 1, 2, 3])

    # Example 2
    run_test(2, 5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]], [3, 4])

    # Example 3
    run_test(3, 3, 2, [[1, 2], [0, 1], [2, 0]], [])

    # Custom Case 4: Disconnected graph, k is isolated
    run_test(4, 4, 2, [[0, 1]], [0, 1, 3])

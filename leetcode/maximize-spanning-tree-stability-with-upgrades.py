class Solution(object):
    def maxStability(self, n, edges, k):
        must_1 = []
        must_0 = []
        parent_pre = list(range(n))

        def find_pre(i):
            while parent_pre[i] != i:
                parent_pre[i] = parent_pre[parent_pre[i]]
                i = parent_pre[i]
            return i

        def union_pre(i, j):
            root_i = find_pre(i)
            root_j = find_pre(j)
            if root_i != root_j:
                parent_pre[root_i] = root_j
                return True
            return False

        for u, v, s, m in edges:
            if m == 1:
                must_1.append((u, v, s))
                if not union_pre(u, v):
                    return -1
            else:
                must_0.append((u, v, s))
        if len(must_1) > n - 1:
            return -1

        def can_form_mst(mid):
            parent = list(range(n))

            def find(i):
                while parent[i] != i:
                    parent[i] = parent[parent[i]]
                    i = parent[i]
                return i

            def union(i, j):
                root_i = find(i)
                root_j = find(j)
                if root_i != root_j:
                    parent[root_i] = root_j
                    return True
                return False

            comps = n
            for u, v, s in must_1:
                if s < mid:
                    return False
                if union(u, v):
                    comps -= 1
            if comps == 1:
                return True

            cost_1_edges = []
            for u, v, s in must_0:
                if s >= mid:
                    if union(u, v):
                        comps -= 1
                        if comps == 1:
                            return True
                elif s * 2 >= mid:
                    cost_1_edges.append((u, v))

            upgrades = 0
            for u, v in cost_1_edges:
                if union(u, v):
                    comps -= 1
                    upgrades += 1
                    if comps == 1:
                        break
            return comps == 1 and upgrades <= k

        ans = -1
        low = 1
        high = min([s for u, v, s in must_1]) if must_1 else 200000

        while low <= high:
            mid = (low + high) // 2
            if can_form_mst(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, edges, k, expected):
        result = solver.maxStability(n, edges, k)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    n = {n}, k = {k}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, 3, [[0, 1, 2, 1], [1, 2, 3, 0]], 1, 2)

    # Example 2
    run_test(2, 3, [[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]], 2, 6)

    # Example 3 (Cycle in Mandatory edges)
    run_test(3, 3, [[0, 1, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]], 0, -1)

    # Custom Case: Cannot connect all components
    run_test(4, 3, [[0, 1, 1, 0]], 1, -1)

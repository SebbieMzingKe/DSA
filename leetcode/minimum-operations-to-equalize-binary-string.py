from collections import deque


class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        initial_z = s.count("0")
        if initial_z == 0:
            return 0
        
        parent = list(range(n + 3))

        def find(i):
            if parent[i] == i:
                return i
            
            parent[i] = find(parent[i])

            return parent[i]

        queue = deque([(initial_z, 0)])
        parent[initial_z] = initial_z + 2

        while queue:
            curr_z, dist = queue.popleft()
            L = abs(curr_z - k)
            R = curr_z + k - 2 * max(0, k - (n - curr_z))

            nxt = find(L)
            while nxt <= R:
                if nxt == 0:
                    return dist + 1

                queue.append((nxt, dist + 1))
                parent[nxt] = nxt + 2
                nxt = find(nxt)
        
        return -1

if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s, k, expected):
        result = solver.minOperations(s, k)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: s='{s}', k={k} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # 1 zero. k=1. Flip it directly.
    run_test(1, "110", 1, 1)

    # Example 2
    # "0101" -> 2 zeros. k=3. Optimal operations = 2
    run_test(2, "0101", 3, 2)

    # Example 3
    # "101" -> 1 zero. k=2. Impossible to flip exactly 2 to get all 1s.
    run_test(3, "101", 2, -1)

    # Custom Case: All 0s
    # "0000", k=2. Flip [0,1], then [2,3].
    run_test(4, "0000", 2, 2)

    # Custom Case: Already 1s
    run_test(5, "1111", 2, 0)

class Solution(object):
    def longestBalanced(self, nums):
        n = len(nums)
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node):
            if lazy[node] != 0:
                lz = lazy[node]
                left, right = 2 * node, 2 * node + 1
                tree_min[left] += lz
                tree_max[left] += lz
                lazy[left] += lz
                tree_min[right] += lz
                tree_max[right] += lz
                lazy[right] += lz
                lazy[node] = 0

        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return

            if l <= start and end <= r:
                tree_min[node] += val
                tree_max[node] += val
                lazy[node] += val

                return
            push(node)

            mid = (start + end) // 2

            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)

            tree_min[node] = min(tree_min[2 * node], tree_min[2 * node + 1])
            tree_max[node] = max(tree_max[2 * node], tree_max[2 * node + 1])

        def find_first_zero(node, start, end, limit):
            if tree_min[node] > 0 or tree_max[node] < 0:
                return -1

            if start > limit:
                return -1

            if start == end:
                return start if tree_min[node] == 0 else -1

            push(node)

            mid = (start + end) // 2

            res = -1

            if start <= limit:
                res = find_first_zero(2 * node, start, mid, limit)

            if res != -1:
                return res

            if mid + 1 <= limit:
                return find_first_zero(2 * node + 1, mid + 1, end, limit)

            return -1

        last_pos = {}
        max_len = 0

        for r in range(n):
            val = nums[r]

            diff = 1 if (val % 2 != 0) else -1

            prev = last_pos.get(val, -1)
            update(1, 0, n - 1, prev + 1, r, diff)
            last_pos[val] = r
            l = find_first_zero(1, 0, n - 1, r)

            if l != -1:
                max_len = max(max_len, r - l + 1)
        return max_len


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.longestBalanced(nums)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: {nums} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # [2, 5, 4, 3] -> 2 even, 2 odd. Balanced. Len 4.
    run_test(1, [2, 5, 4, 3], 4)

    # Example 2
    # [3, 2, 2, 5, 4] -> Balanced [3, 2, 2, 5, 4] (odds: 3,5; evens: 2,4). Len 5.
    run_test(2, [3, 2, 2, 5, 4], 5)

    # Example 3
    # [1, 2, 3, 2] -> Balanced [2, 3, 2] (even 2, odd 3). Len 3.
    run_test(3, [1, 2, 3, 2], 3)

    # Custom Case: Single Type
    # [2, 4, 6] -> 3 evens, 0 odds. Not balanced.
    run_test(4, [2, 4, 6], 0)

    # Custom Case: Interleaved duplicates
    # [1, 2, 1, 2] -> Balanced.
    run_test(5, [1, 2, 1, 2], 4)

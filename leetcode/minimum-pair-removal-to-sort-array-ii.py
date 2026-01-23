import heapq


class Solution(object):
    def minimumPairRemoval(self, nums):

        n = len(nums)

        if n <= 1:
            return 0

        vals = list(nums)

        left = [i - 1 for i in range(n)]
        right = [i + 1 for i in range(n)]

        right[n - 1] = -1

        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (vals[i] + vals[i + 1], i))

        inv_count = 0

        for i in range(n - 1):
            if vals[i] > vals[i + 1]:
                inv_count += 1

        if inv_count == 0:
            return 0

        removed = [False] * n
        ops = 0

        while inv_count > 0:
            if not pq:
                break

            s, i = heapq.heappop(pq)

            if removed[i]:
                continue

            j = right[i]

            if j == -1:
                continue

            if vals[i] + vals[j] != s:
                continue

            ops += 1
            left_index, right_index = left[i], right[j]

            if vals[i] > vals[j]:
                inv_count -= 1

            if left_index != -1 and vals[left_index] > vals[i]:
                inv_count -= 1
            if right_index != -1 and vals[j] > vals[right_index]:
                inv_count -= 1

            vals[i] += vals[j]
            removed[j] = True
            right[i] = right_index
            if right_index != -1:
                left[right_index] = i

            if left_index != -1 and vals[left_index] > vals[i]:
                    inv_count += 1
            if right_index != -1 and vals[i] > vals[right_index]:
                inv_count += 1

            if left_index != -1:
                heapq.heappush(pq, (vals[left_index] + vals[i], left_index))

            if right_index != -1:
                heapq.heappush(pq, (vals[i] + vals[right_index], i))

        return ops


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.minimumPairRemoval(nums)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: Input {nums} -> Output {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    run_test(1, [5, 2, 3, 1], 2)

    # Example 2 (Already Sorted)
    run_test(2, [1, 2, 2], 0)

    # Large Tie Breaker Case
    # Pairs (1,1)=2 at indices 1 and 2. Leftmost (idx 1) should be picked.
    run_test(3, [5, 1, 1, 1, 5], 3)

    # Reverse Sorted Case
    run_test(4, [3, 2, 1], 1)

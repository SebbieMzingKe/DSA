from ast import List
import heapq
from typing import Counter


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:

        k -= 1
        n = len(nums)

        lower = []
        lower_sum = 0
        lower_size = 0

        upper = []
        upper_size = 0

        out_counts = Counter()

        def clean_tops():
            # Remove invalid elements from the top of heaps
            while lower and out_counts[-lower[0]] > 0:
                out_counts[-lower[0]] -= 1
                heapq.heappop(lower)
            while upper and out_counts[upper[0]] > 0:
                out_counts[upper[0]] -= 1
                heapq.heappop(upper)

        def push_lower(val):
            nonlocal lower_sum, lower_size
            heapq.heappush(lower, -val)
            lower_sum += val
            lower_size += 1

        def push_upper(val):
            nonlocal upper_size
            heapq.heappush(upper, val)
            upper_size += 1

        def pop_lower():
            nonlocal lower_sum, lower_size
            clean_tops()
            val = -heapq.heappop(lower)
            lower_sum -= val
            lower_size -= 1
            return val

        def pop_upper():
            nonlocal upper_size
            clean_tops()
            val = heapq.heappop(upper)
            upper_size -= 1
            return val

        window_end = min(n, dist + 2)

        for i in range(1, window_end):
            val = nums[i]
            push_upper(val)

        while lower_size < k and upper:
            push_lower(pop_upper())

        min_cost = lower_sum

        for i in range(window_end, n):
            in_val = nums[i]
            out_val = nums[i - (dist + 1)]

            clean_tops()
            max_lower = -lower[0]

            if out_val <= max_lower:
                # It's in Lower (or equal to the boundary)
                lower_sum -= out_val
                lower_size -= 1
                out_counts[out_val] += 1
            else:
                # It's in Upper
                upper_size -= 1
                out_counts[out_val] += 1

            clean_tops()
            # If lower is not empty and in_val is smaller than Lower's max, it belongs in Lower
            if lower and in_val < -lower[0]:
                push_lower(in_val)
            else:
                push_upper(in_val)

            while lower_size < k:
                clean_tops()
                push_lower(pop_upper())

            while lower_size > k:
                clean_tops()
                push_upper(pop_lower())

            # Update minimum cost
            if lower_sum < min_cost:
                min_cost = lower_sum

        return min_cost + nums[0]


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, k, dist, expected):
        result = solver.minimumCost(nums, k, dist)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Cost: 1 + (3 or 2 from window [3,2,6,4])
    # k=3 -> need 2 elements.
    # Window [3,2,6,4] (size dist+1=4). Smallest 2 are 2,3. Sum=5. +1 = 6?
    # Wait, example explanation: [1,3], [2,6,4], [2]. Heads: 1, 2, 2.
    # Indices: 0, 2, 5. i2-i1 = 5-2 = 3 <= 3. Valid. Cost 1+2+2 = 5.
    run_test(1, [1, 3, 2, 6, 4, 2], 3, 3, 5)

    # Example 2
    # k=4 -> Need 3 elements. dist=3.
    # Window size 4.
    # Optimal: Heads 10, 1, 2, 2. Indices 0, 1, 2, 3.
    # Dist 3-1 = 2 <= 3. Cost 15.
    run_test(2, [10, 1, 2, 2, 2, 1], 4, 3, 15)

    # Example 3
    # k=3 -> Need 2 elements. dist=1.
    # Window size 2.
    # Window [8, 18]. Smallest 2: 8, 18. Sum 26. +10 = 36.
    run_test(3, [10, 8, 18, 9], 3, 1, 36)

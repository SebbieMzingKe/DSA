import bisect
from collections import defaultdict

class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)

        val_to_indices = defaultdict(list)

        for i, num in enumerate(nums):
            val_to_indices[num].append(i)
        
        ans = []

        for q_idx in queries:
            val = nums[q_idx]
            indices = val_to_indices[val]

            if len(indices) == 1:
                ans.append(-1)
                continue

            pos = bisect.bisect_left(indices, q_idx)

            left_pos = (pos - 1) %len(indices)
            right_pos = (pos + 1) %len(indices)

            left_idx = indices[left_pos]
            right_idx = indices[right_pos]

            dist_left = abs(q_idx - left_idx)
            circ_dist_left = min(dist_left, n - dist_left)

            dist_right = abs(q_idx - right_idx)
            circ_dist_right = min(dist_right, n - dist_left)

            ans.append(min(circ_dist_left, circ_dist_right))
        
        return ans




if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums, queries, expected):
        result = solver.solveQueries(nums, queries)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Nums:     {nums}")
        print(f"  Queries:  {queries}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [1, 3, 1, 4, 1, 3, 2], [0, 3, 5], [2, -1, 3])

    # Example 2
    run_test(2, [1, 2, 3, 4], [0, 1, 2, 3], [-1, -1, -1, -1])

    # Custom Case 3: Only two elements, wrap-around is shortest
    run_test(3, [5, 1, 1, 1, 5], [0], [1])
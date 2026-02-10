class Solution(object):
    def getLongestSubarray(self, nums):
        n = len(nums)
        max_len = 0

        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            

            for j in range(i, n):
                val = nums[j]

                if val % 2 == 0:
                    distinct_evens.add(val)
                
                else:
                    distinct_odds.add(val)

                
                if len(distinct_evens) == len(distinct_odds):
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
            
        return max_len


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.getLongestSubarray(nums)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: {nums} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # [2,5,4,3] -> Distinct Evens {2,4}, Distinct Odds {5,3}. Count 2==2. Len 4.
    run_test(1, [2, 5, 4, 3], 4)

    # Example 2
    # [3,2,2,5,4] -> Evens {2,4}, Odds {3,5}. Count 2==2. Len 5.
    run_test(2, [3, 2, 2, 5, 4], 5)

    # Example 3
    # [1,2,3,2] -> Subarray [2,3,2] has Even {2}, Odd {3}. Count 1==1. Len 3.
    run_test(3, [1, 2, 3, 2], 3)

    # Edge Case: Single element
    # [2] -> Even 1, Odd 0. Not balanced.
    run_test(4, [2], 0)

    # Edge Case: Empty
    run_test(5, [], 0)

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        n, m = len(nums1), len(nums2)

        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                current_product = nums1[i - 1] * nums2[j - 1]

                prev_diagonal = dp[i - 1][j - 1]
                option_include = current_product + max(0, prev_diagonal)

                option_skip_i = dp[i - 1][j]

                option_skip_j = dp[i][j - 1]

                dp[i][j] = max(option_include, option_skip_i, option_skip_j)
        
        return int(dp[n][m])
    
if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums1, nums2, expected):
        result = solver.maxDotProduct(nums1, nums2)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Subsequences: [2, -2] and [3, -6] -> 2*3 + (-2)*(-6) = 6 + 12 = 18
    run_test(1, [2,1,-2,5], [3,0,-6], 18)
    
    # Example 2
    # Subsequences: [3] and [7] -> 21
    run_test(2, [3,-2], [2,-6,7], 21)
    
    # Example 3 (Negative answer case)
    # Subsequences: [-1] and [1] -> -1 (Must pick non-empty)
    run_test(3, [-1,-1], [1,1], -1)

    # Edge Case: Single elements
    run_test(4, [-5], [5], -25)
    
    # Edge Case: All zeros
    run_test(5, [0, 0], [1, -5], 0)
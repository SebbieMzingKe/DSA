class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        n = len(strs)
        m = len(strs[0])

        dp = [1] * m

        for i in range(m):
            for j in range(i):
                is_valid_sequence = True
                for row in range(n):
                    if strs[row][j] > strs[row][i]:
                        is_valid_sequence = False
                        break
                
                if is_valid_sequence:
                    dp[i] = max(dp[i], dp[j] + 1)

        return m - max(dp)


if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    # Keep columns 1 ('a') and 4 ('a'). Subsequence length 2.
    # Total 5. Deletions = 5 - 2 = 3.
    s1 = ["babca","bbazb"]
    print(f"Test Case 1: {solver.minDeletionSize(s1)} (Expected: 3)")
    
    # Example 2
    # Only 1 column can be kept (any single char). LIS is 1.
    # Total 5. Deletions = 5 - 1 = 4.
    s2 = ["edcba"]
    print(f"Test Case 2: {solver.minDeletionSize(s2)} (Expected: 4)")
    
    # Example 3
    # Already sorted. Keep all 3. Deletions 0.
    s3 = ["ghi","def","abc"]
    print(f"Test Case 3: {solver.minDeletionSize(s3)} (Expected: 0)")
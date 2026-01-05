class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
         """

        total_sum= 0
        min_abs = float('inf')
        neg_count = 0

        for row in matrix:
            for val in row:
                total_sum += abs(val)

                min_abs = min(min_abs, abs(val))

                if val < 0:
                    neg_count += 1

                
        if neg_count % 2 == 0:
            return total_sum

        return total_sum - (2 * min_abs)
    

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, matrix, expected):
        result = solver.maxMatrixSum(matrix)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # [-1, -1] -> 2 negatives (even) -> All become positive -> 1+1+1+1 = 4
    matrix1 = [[1, -1], [-1, 1]]
    run_test(1, matrix1, 4)
    
    # Example 2
    # [-1, -2, -3] -> 3 negatives (odd)
    # Smallest abs is 1. Total abs sum is 18.
    # Result = 18 - 2(1) = 16
    matrix2 = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
    run_test(2, matrix2, 16)

    # Edge Case: Single negative which is also the smallest
    # [[5, 5], [5, -1]] -> Total abs 16. Odd negs. Smallest 1. 
    # Result = 16 - 2 = 14.
    matrix3 = [[5, 5], [5, -1]]
    run_test(3, matrix3, 14)
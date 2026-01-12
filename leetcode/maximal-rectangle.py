class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if not matrix:
            return 0
            
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            for i, val in enumerate(row):
                # Update histogram heights
                if val == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            

    
            # Calculate max area for the current row's histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
            
        return max_area

    def largestRectangleArea(self, heights):
        # Add a 0 at the end to force the stack to empty
        stack = [-1]
        max_area = 0


        for i in range(len(heights) + 1):
            current_h = heights[i] if i < len(heights) else 0
            
            while len(stack) > 1 and current_h < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            
            stack.append(i)
            
        return max_area

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, matrix, expected):
        result = solver.maximalRectangle(matrix)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    matrix1 = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    run_test(1, matrix1, 6)

    # Example 2
    matrix2 = [["0"]]
    run_test(2, matrix2, 0)

    # Example 3
    matrix3 = [["1"]]
    run_test(3, matrix3, 1)

    # Example 4: Full square
    matrix4 = [
        ["1","1"],
        ["1","1"]
    ]
    run_test(4, matrix4, 4)
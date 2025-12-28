class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        count = 0
        row = m - 1
        col = 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:

                count += (n - col)

                row -= 1
            else:
                col += 1

        return count
    

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    # Row 0: 4, 3, 2, -1 (1 neg)
    # Row 1: 3, 2, 1, -1 (1 neg)
    # Row 2: 1, 1, -1, -2 (2 neg)
    # Row 3: -1, -1, -2, -3 (4 neg)
    # Total: 1 + 1 + 2 + 4 = 8
    grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(f"Test Case 1: {solver.countNegatives(grid1)} (Expected: 8)")
    
    # Example 2
    # No negatives
    grid2 = [[3,2],[1,0]]
    print(f"Test Case 2: {solver.countNegatives(grid2)} (Expected: 0)")
    
    # Example 3
    # All negatives
    grid3 = [[-1,-2],[-3,-4]]
    print(f"Test Case 3: {solver.countNegatives(grid3)} (Expected: 4)")
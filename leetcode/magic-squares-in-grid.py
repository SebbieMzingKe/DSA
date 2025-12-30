class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        if rows < 3 or cols < 3:
            return 0
        
        def is_magic(r, c):
            if grid[r + 1][c + 1] != 5:
                return False
            
            vals = [
                grid[r][c], grid[r][c + 1], grid[r][c + 2],
                grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2],
            ]

            if sorted(vals) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            
            if (grid[r][c] + grid[r + 1][c] + grid[r + 2][c] != 15 or
                grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] != 15 or
                grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] != 15):
                return False
            
            if (grid[r][c] + grid[r][c + 1] + grid[r][c + 2] != 15 or
                grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] != 15 or
                grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] != 15):
                return False
          
            if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or
                grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15):
                return False
            
            return True
            
        count = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1

        return count


if __name__ == "__main__":
    solver = Solution()
    
    grid1 = [[4,3,8,4],
             [9,5,1,9],
             [2,7,6,2]]
    print(f"Test Case 1: {solver.numMagicSquaresInside(grid1)} (Expected: 1)")
    
    grid2 = [[8]]
    print(f"Test Case 2: {solver.numMagicSquaresInside(grid2)} (Expected: 0)")
    
    grid3 = [[4,3,8],
             [9,5,1],
             [2,7,10]]
    print(f"Test Case 3: {solver.numMagicSquaresInside(grid3)} (Expected: 0)")
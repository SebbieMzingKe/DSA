import collections


class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """

        left, right = 1, len(cells)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if self.canCross(row, col, mid, cells):
                answer = mid
                left = mid + 1

            else:
                right = mid - 1

        return answer
    
    def canCross(self, row, col, day, cells):
        """
        helper function to check if path exists from top to bottom after day number of cells have been flooded
        """

        grid = [[0] * col for _ in range(row)]

        for i in range(day):
            r, c = cells[i]
            grid[r - 1][c - 1] = 1

        queue = collections.deque()


        for c in range(col):
            if grid[0][c] == 0:
                queue.append((0, c))
                grid[0][c] = 1

        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()

            if r == row - 1:

                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc))
        
        return False

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    # Grid starts empty.
    # Day 1: (1,1) water. Path exists? Yes.
    # Day 2: (2,1) water. Path exists? Yes.
    # Day 3: (1,2) water. Top row blocked? Maybe.
    # Expected Output: 2
    row1, col1 = 2, 2
    cells1 = [[1,1],[2,1],[1,2],[2,2]]
    print(f"Test Case 1: {solver.latestDayToCross(row1, col1, cells1)} (Expected: 2)")
    
    # Example 2
    row2, col2 = 2, 2
    cells2 = [[1,1],[1,2],[2,1],[2,2]]
    print(f"Test Case 2: {solver.latestDayToCross(row2, col2, cells2)} (Expected: 1)")
    
    # Example 3
    row3, col3 = 3, 3
    cells3 = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
    print(f"Test Case 3: {solver.latestDayToCross(row3, col3, cells3)} (Expected: 3)")
class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """

        matrix = [[0] * n for _ in range(m)]
        # 0 -> free 1 -> wall 2 -> guardable position 3 -> guards

        for r, c in guards:
            matrix[r][c] = 1
        for r, c in walls:
            matrix[r][c] = 2

        # moving up, down etc
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # helper function to mark guarded cells
        def mark_guarded(r, c):
            for dr, dc in directions:
                # nr/c -> next row/column
                nr, nc = r + dr, c + dc
                
                while 0 <= nr < m and 0 <= nc < n:
                    if matrix[nr][nc] in [1, 2]: # if it hits guard or wall
                        break
                    matrix[nr][nc] = 3 # therefore mark it as guarded
                    nr += dr
                    nc += dc
        
        for r, c in guards:
            mark_guarded(r, c)

        return sum(cell == 0 for row in matrix for cell in row)
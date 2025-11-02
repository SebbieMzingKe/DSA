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
        # 1 -> free 2 -> wall 3 -> guardable position 

        for r, c in guards:
            matrix[r][c] = 1
        for r, c in walls:
            matrix[r][c] = 2
        
        # helper function to mark guarded cells
        def mark_guarded(r, c):
            for row in range(r + 1, m):
                if matrix[row][c] in [1, 2]:
                    break
                matrix[row][c] = 3
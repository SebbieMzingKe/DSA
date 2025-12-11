class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """

        row_min = {}
        row_max = {}
        col_min = {}
        col_max = {}

        for x, y in buildings:

            if x not in row_min:
                row_min[x] = y
                row_max[x] = y

            else:
                if y < row_min[x]:
                    row_min[x] = y
                
                if y > row_max[x]:
                    row_max[x] = y
            
            if y not in col_min:
                col_min[y] = y
                col_max[y] = y

            else:
                if x < col_min[y]:
                    col_min[y] = x
                
                if x > col_max[y]:
                    col_max[y] = x

        count = 0

        for x, y in buildings:

            if y == row_min[x] or y == row_max[x]:
                continue

            if x == col_min[y] or x == col_max[y]:
                continue

            count += 1
        
        return count
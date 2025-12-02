from collections import defaultdict


class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        y_counts = defaultdict(int)
        
        for x, y in points:
            y_counts[y] += 1
        
        result = 0
        prev_sum = 0

        for count in y_counts.values():
            if count >= 2:
                curr = count * (count -1) // 2

                result = (result + curr * prev_sum) % MOD
                prev_sum = (prev_sum + curr) % MOD

        return result
from math import sqrt


class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = 0

        for a in range(a, n + 1):
            for b in range(a, a + 1):
                c_squared = a * a + b * b
                c = int(sqrt(c_squared))

                if c <= n and c * c == c_squared:
                    result += 2 if a != b else 1
        
        return result
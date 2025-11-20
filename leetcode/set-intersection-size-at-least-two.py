class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda i: (i[1], i[0]))

        result = 0
        p1, p2 = -1, -1

        for start, end in intervals:
            if p2 < start:
                result += 2
                p1, p2 = end - 1, end

            elif p1 < start:
                result += 1
                if p2 == end:
                    p1 = end -1
                
                else:
                    p1, p2 = p2, end
        return result
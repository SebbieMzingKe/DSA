class Solution(object):
    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def _norm(self, a, b):
        """Return reduced fraction (a/b) as canonical tuple."""
        if a == 0 and b == 0:
            return (0, 0)
        g = self._gcd(abs(a), abs(b))
        a //= g
        b //= g
        # Keep denominator positive
        if b < 0:
            a = -a
            b = -b
        return (a, b)
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        # First pass: count trapezoids + parallelograms
        trapezium_parallelograms = 0
        parallel_lines = {}        # slope -> count
        collinear_lines = {}       # (slope, intercept) -> count

        for i in range(n):
            x2, y2 = points[i]
            for j in range(i):
                x1, y1 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # slope
                if dx != 0:
                    slope = self._norm(dy, dx)
                else:
                    slope = ("inf", 0)

                # intercept
                if dx != 0:
                    intercept = self._norm(y1 * dx - dy * x1, dx)
                else:
                    intercept = (x1, 1)

                slope_key = slope
                full_line_key = (slope, intercept)

                seen_parallel = parallel_lines.get(slope_key, 0)
                seen_collinear = collinear_lines.get(full_line_key, 0)

                trapezium_parallelograms += seen_parallel - seen_collinear

                parallel_lines[slope_key] = seen_parallel + 1
                collinear_lines[full_line_key] = seen_collinear + 1

        # Second pass: count parallelograms using distance
        parallelograms = 0
        parallel_lines_dist = {}
        collinear_lines_dist = {}

        for i in range(n):
            x2, y2 = points[i]
            for j in range(i):
                x1, y1 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx != 0:
                    slope = self._norm(dy, dx)
                    intercept = self._norm(y1 * dx - dy * x1, dx)
                else:
                    slope = ("inf", 0)
                    intercept = (x1, 1)

                dist = dx * dx + dy * dy

                slope_dist_key = (slope, dist)
                full_line_dist_key = (slope, intercept, dist)

                seen_parallel_dist = parallel_lines_dist.get(slope_dist_key, 0)
                seen_collinear_dist = collinear_lines_dist.get(full_line_dist_key, 0)

                parallelograms += seen_parallel_dist - seen_collinear_dist

                parallel_lines_dist[slope_dist_key] = seen_parallel_dist + 1
                collinear_lines_dist[full_line_dist_key] = seen_collinear_dist + 1

        return trapezium_parallelograms - parallelograms // 2
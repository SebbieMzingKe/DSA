class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        total_time = 0

        for i in range(1, len(points)):
            prev = points[i - 1]
            curr = points[i]

            dx = abs(curr[0] - prev[0])
            dy = abs(curr[1] - prev[1])

            total_time += max(dx, dy)

        return total_time
    

if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, points, expected):
        result = solver.minTimeToVisitAllPoints(points)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {points} -> {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Path: [1,1] -> [3,4] (diff: 2, 3 -> time 3)
    #       [3,4] -> [-1,0] (diff: 4, 4 -> time 4)
    # Total: 7
    run_test(1, [[1,1], [3,4], [-1,0]], 7)

    # Example 2
    # Path: [3,2] -> [-2,2] (diff: 5, 0 -> time 5)
    run_test(2, [[3,2], [-2,2]], 5)
    
    # Edge Case: Single movement (Diagonal)
    run_test(3, [[0,0], [2,2]], 2)

    # Edge Case: Vertical movement only
    run_test(4, [[0,0], [0,5]], 5)
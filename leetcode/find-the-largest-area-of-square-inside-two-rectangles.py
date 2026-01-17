class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """

        max_side = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):

                overlap_min_x = max(bottomLeft[i][0], bottomLeft[j][0])
                overlap_min_y = max(bottomLeft[i][1], bottomLeft[j][1])

                overlap_max_x = min(topRight[i][0], topRight[j][0])
                overlap_max_y = min(topRight[i][1], topRight[j][i])

                width = overlap_max_x - overlap_min_x
                height = overlap_max_y - overlap_min_y

                if width > 0 and height > 0:

                    current_side = min(width, height)

                    if current_side > max_side:
                        max_side = current_side

        return max_side * max_side


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, bl, tr, expected):
        result = solver.largestSquareArea(bl, tr)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Rect 0: [1,1] to [3,3]
    # Rect 1: [2,2] to [4,4]
    # Intersect 0&1: [2,2] to [3,3] -> w=1, h=1 -> side=1 -> Area 1
    bl1 = [[1, 1], [2, 2], [3, 1]]
    tr1 = [[3, 3], [4, 4], [6, 6]]
    run_test(1, bl1, tr1, 1)

    # Example 2
    # Overlap is [1,5] to [5,7] -> w=4, h=2 -> side=2 -> Area 4
    bl2 = [[1, 1], [1, 3], [1, 5]]
    tr2 = [[5, 5], [5, 7], [5, 9]]
    run_test(2, bl2, tr2, 4)

    # Example 4: No overlap
    bl3 = [[1, 1], [3, 3], [3, 1]]
    tr3 = [[2, 2], [4, 4], [4, 2]]
    run_test(3, bl3, tr3, 0)

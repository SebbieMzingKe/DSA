class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """

        MOD =10 ** 9 + 7
        seats = []

        # indicess
        for i, char in enumerate(corridor):
            if char == "S":
                seats.append(i)

        if len(seats) == 0 or len(seats) % 2 != 0:
            return 0

        answer = 1
        
        for i in range(2, len(seats), 2):
            prev_end = seats[i - 1]
            next_start = seats[i]

            ways_to_divide = next_start - prev_end
            answer = (answer * ways_to_divide) % MOD


        return answer

if __name__ == "__main__":
    solver = Solution()

    # Example 1
    # Seats at indices: 0, 1, 4, 6
    # Pair 1: (0,1), Pair 2: (4,6)
    # Gap between 1 and 4 is (4 - 1) = 3 ways.
    c1 = "SSPPSPS"
    print(f"Test Case 1: {solver.numberOfWays(c1)} (Expected: 3)")

    # Example 2
    # Seats at indices: 2, 4
    # Pair 1: (2,4). No gaps between pairs needed. Result 1.
    c2 = "PPSPSP"
    print(f"Test Case 2: {solver.numberOfWays(c2)} (Expected: 1)")

    # Example 3
    # Seats at indices: 0. Count is 1 (odd). Result 0.
    c3 = "S"
    print(f"Test Case 3: {solver.numberOfWays(c3)} (Expected: 0)")
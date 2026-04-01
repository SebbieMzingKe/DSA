class Solution(object):
    def survivedRobotsHealth(self, positions, healths, directions):
        n = len(positions)
        robots = [[positions[i], healths[i], directions[i], 1] for i in range(n)]
        robots.sort(key=lambda x: x[0])

        stack = []

        for robot in robots:
            if robot[2] == "R":
                stack.append(robot)
            else:
                survived = True
                while stack and stack[-1][2] == "R":
                    if robot[1] > stack[-1][1]:
                        stack.pop()
                        robot[1] -= 1

                    elif robot[1] < stack[-1][1]:
                        stack[-1][1] -= 1
                        survived = False
                        break

                    else:
                        stack.pop()
                        survived = False
                        break

                if survived:
                    stack.append(robot)
        stack.sort(key=lambda x: x[3])
        return [robot[1] for robot in stack]


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, positions, healths, directions, expected):
        result = solver.survivedRobotsHealths(positions, healths, directions)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Positions:  {positions}")
        print(f"  Healths:    {healths}")
        print(f"  Directions: '{directions}'")
        print(f"  Output:     {result}")
        print(f"  Expected:   {expected}")
        print(f"  Status:     {status}\n")

    # Example 1: All moving same direction
    run_test(1, [5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR", [2, 17, 9, 15, 10])

    # Example 2: Sequential collisions
    run_test(2, [3, 5, 2, 6], [10, 10, 15, 12], "RLRL", [14])

    # Example 3: Total mutual destruction
    run_test(3, [1, 2, 5, 6], [10, 10, 11, 11], "RLRL", [])

    # Custom Case 4: A single massive 'L' robot wiping out multiple 'R' robots
    run_test(4, [1, 2, 3, 4, 5], [1, 1, 1, 1, 10], "RRRRL", [6])

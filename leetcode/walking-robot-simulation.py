class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y, d = 0, 0, 0
        obstacle_set = set(map(tuple, obstacles))
        max_dist_sq = 0

        for cmd in commands:
            if cmd == -2:
                d = (d - 1) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                for _ in range(cmd):
                    nx, ny = x + dx[d], y + dy[d]
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    max_dist_sq = max(max_dist_sq, x * x + y * y)

        return max_dist_sq


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, commands, obstacles, expected):
        result = solver.robotSim(commands, obstacles)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Commands:  {commands}")
        print(f"  Obstacles: {obstacles}")
        print(f"  Output:    {result}")
        print(f"  Expected:  {expected}")
        print(f"  Status:    {status}\n")

    # Example 1
    run_test(1, [4, -1, 3], [], 25)

    # Example 2
    run_test(2, [4, -1, 4, -2, 4], [[2, 4]], 65)

    # Example 3
    run_test(3, [6, -1, -1, 6], [[0, 0]], 36)

    # Custom Case: Origin obstacle ignored initially, then blocks return
    run_test(4, [2, -1, -1, 2], [[0, 0]], 4)

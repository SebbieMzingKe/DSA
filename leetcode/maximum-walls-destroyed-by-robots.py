import bisect


class Solution(object):
    def maxWalls(self, robots, distance, walls):
        robots_data = sorted(zip(robots, distance))
        walls.sort()

        def count_walls(left_bound, right_bound):
            if left_bound > right_bound:
                return 0
            return bisect.bisect_right(walls, right_bound) - bisect.bisect_left(
                walls, left_bound
            )

        robots_set = set(robots)
        w_base = len(set(walls).intersection(robots_set))
        N = len(robots_data)

        p0, d0 = robots_data[0]
        prev_L = count_walls(p0 - d0, p0 - 1)
        prev_R = 0

        for i in range(1, N):
            p_prev, d_prev = robots_data[i - 1]
            p_curr, d_curr = robots_data[i]

            r_reach = min(p_curr - 1, p_prev + d_prev)
            l_reach = max(p_prev + 1, p_curr - d_curr)

            c_LL = count_walls(l_reach, p_curr - 1)
            c_RR = count_walls(p_prev + 1, r_reach)
            c_LR = 0

            if r_reach < l_reach:
                c_RL = c_RR + c_LL
            else:
                c_RL = count_walls(p_prev + 1, p_curr - 1)

            curr_L = max(prev_L + c_LL, prev_R + c_RL)
            curr_R = max(prev_L + c_LR, prev_R + c_RR)

            prev_L, prev_R = curr_L, curr_R

        pN, dN = robots_data[-1]
        ans = max(prev_L, prev_R + count_walls(pN + 1, pN + dN))
        return ans + w_base


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, robots, distance, walls, expected):
        result = solver.maxWalls(robots, distance, walls)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Robots:   {robots}")
        print(f"  Distance: {distance}")
        print(f"  Walls:    {walls}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [4], [3], [1, 10], 1)

    # Example 2
    run_test(2, [10, 2], [5, 1], [5, 2, 7], 3)

    # Example 3
    run_test(3, [1, 2], [100, 1], [10], 0)

    # Custom Case 4: Overlapping Robot Coverage check
    run_test(4, [2, 10], [5, 5], [3, 4, 5, 8, 9], 5)

import collections

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """

        transitions = collections.defaultdict(list)

        for pattern in allowed:
            left, right, top = pattern[0], pattern[1], pattern[2]
            transitions[(left, right)].append(top)


        failed_rows = set()

        def dfs(current_row):
            """
            tries to build the pyramid upwards from the current_row.
            returns True if successful, False otherwise.
            """

            if len(current_row) == 1:
                return True

            if current_row in failed_rows:
                return False
            
            def generate_next_rows(index, path):
                """
                recursively builds the next row.
                index: current position in current_row we are processing
                path: list of blocks chosen so far for the next row
                """

                if index == len(current_row) - 1:
                    yield "".join(path)

                    return

                left = current_row[index]
                right = current_row[index + 1]

                if (left, right) in transitions:
                    for top in transitions[(left, right)]:
                        path.append(top)

                        for res in generate_next_rows(index + 1, path):
                            yield res
                        path.pop()

            
            for next_row in generate_next_rows(0, []):
                if dfs(next_row):
                    return True

            failed_rows.add(current_row)
            return False

        return dfs(bottom)
    

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    # Valid Path: BCD -> CE -> A
    bottom1 = "BCD"
    allowed1 = ["BCC","CDE","CEA","FFF"]
    print(f"Test Case 1: {solver.pyramidTransition(bottom1, allowed1)} (Expected: True)")
    
    # Example 2
    # AAAA fails because eventual combinations lead to dead ends.
    bottom2 = "AAAA"
    allowed2 = ["AAB","AAC","BCD","BBE","DEF"]
    print(f"Test Case 2: {solver.pyramidTransition(bottom2, allowed2)} (Expected: False)")
    
    # Example 3 (Edge Case)
    # Smallest valid pyramid
    bottom3 = "AB"
    allowed3 = ["ABC"]
    print(f"Test Case 3: {solver.pyramidTransition(bottom3, allowed3)} (Expected: True)")
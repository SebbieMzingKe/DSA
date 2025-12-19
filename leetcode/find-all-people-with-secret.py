import itertools


class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """

        meetings.sort(key = lambda x: x[2])

        known = {0, firstPerson}

        for time, group in itertools.groupby(meetings, key = lambda x: x[2]):
            current_meetings = list(group)

            graph = {}
            participants=set()

            for p1, p2, _ in current_meetings:
                if p1 not in graph: graph[p1] = []
                if p2 not in graph: graph[p2] = []

                graph[p1].append(p2)
                graph[p2].append(p1)
                participants.add(p1)
                participants.add(p2)

            queue = []
            visited_in_batch = set()

            for p in participants:
                if p in known:
                    queue.append(p)
                    visited_in_batch.add(p)

            
            head = 0
            while head < len(queue):
                curr = queue[head]
                head += 1

                if curr in graph:
                    for neighbor in graph[curr]:
                        if neighbor not in visited_in_batch:
                            known.add(neighbor)
                            visited_in_batch.add(neighbor)
                            queue.append(neighbor)

        return list(known)


if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    print(f"Test Case 1: {sorted(solver.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))} (Expected: [0, 1, 2, 3, 5])")

    # Example 2
    print(f"Test Case 2: {sorted(solver.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))} (Expected: [0, 1, 3])")
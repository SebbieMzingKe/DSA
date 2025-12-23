import heapq


class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """

        events.sort()

        max_result = 0
        max_prev = 0
        min_heap = []

        for start, end, value in events:
            while min_heap and min_heap[0][0] < start:
                _, prev_value = heapq.heappop(min_heap)
                max_prev = max(max_prev, prev_value)

            max_result = max(max_result, value + max_prev)

            heapq.heappush(min_heap, (end, value))

        return max_result
    

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    print(f"Test Case 1: {solver.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]])} (Expected: 4)")
    
    # Example 2
    print(f"Test Case 2: {solver.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]])} (Expected: 5)")
    
    # Example 3
    print(f"Test Case 3: {solver.maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]])} (Expected: 8)")
    
    # Edge case: Overlapping events
    print(f"Test Case 4: {solver.maxTwoEvents([[1,5,10],[1,5,20]])} (Expected: 20)")
    
    # Edge case: Adjacent events
    print(f"Test Case 5: {solver.maxTwoEvents([[1,2,10],[3,4,20]])} (Expected: 30)")
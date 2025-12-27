import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        
        ready_rooms = [i for i in range(n)]
        heapq.heapify(ready_rooms)
        
        running_meetings = []
        usage_count = [0] * n
        
        for start, end in meetings:
            # free up rooms that finish before this meeting starts
            while running_meetings and running_meetings[0][0] <= start:
                finish_time, room = heapq.heappop(running_meetings)
                heapq.heappush(ready_rooms, room)
            
            if ready_rooms:
                room = heapq.heappop(ready_rooms)
                heapq.heappush(running_meetings, (end, room))
            else:
                # delay scenario: pop the earliest finishing meeting
                finish_time, room = heapq.heappop(running_meetings)
                new_end = finish_time + (end - start)
                heapq.heappush(running_meetings, (new_end, room))
            
            usage_count[room] += 1
            
        max_usage = -1
        max_room = -1
        for i in range(n):
            if usage_count[i] > max_usage:
                max_usage = usage_count[i]
                max_room = i
        return max_room

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    n1 = 2
    meetings1 = [[0,10],[1,5],[2,7],[3,4]]
    print(f"Test Case 1: {solver.mostBooked(n1, meetings1)} (Expected: 0)")
    
    # Example 2
    n2 = 3
    meetings2 = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    print(f"Test Case 2: {solver.mostBooked(n2, meetings2)} (Expected: 1)")
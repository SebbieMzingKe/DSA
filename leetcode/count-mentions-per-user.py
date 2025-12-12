class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """

        mentions = [0] * numberOfUsers

        back_online_time = [0] * numberOfUsers

        parsed_events = []
        for event in events:
            event_type, event_time_string, event_data = event
            event_time = int(event_time_string)
            priority = 0 if event_type == "OFFLINE" else 1
            parsed_events.append((event_time, priority, event_type, event_data))

        parsed_events.sort(key=lambda x: (x[0], x[1]))


        for time, _, event_type, data in parsed_events:
            if event_type == "OFFLINE":

                user_id = int(data)
                back_online_time[user_id] = time + 60

            elif event_type == "MESSAGE":
                if data == "ALL":

                    for i in range(numberOfUsers):
                        mentions[i] += 1
            
                elif data == "HERE":
                    for i in range(numberOfUsers):
                        
                        if back_online_time[i] <= time:
                            mentions[i] += 1


                else:

                    ids = data.split()
                    for id_str in ids:
                        user_id = int(id_str[2:])
                        mentions[user_id] += 1

        return mentions

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    n1 = 2
    events1 = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
    print(f"Test Case 1: {solver.countMentions(n1, events1)} (Expected: [2, 2])")

    # Test Case 2
    n2 = 2
    events2 = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]
    print(f"Test Case 2: {solver.countMentions(n2, events2)} (Expected: [2, 2])")

    # Test Case 3
    n3 = 2
    events3 = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
    print(f"Test Case 3: {solver.countMentions(n3, events3)} (Expected: [0, 1])")
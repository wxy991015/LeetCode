def findingUsersActiveMinutes(logs: list[list[int]], k: int) -> list[int]:
    answer = [0] * k
    user_active_minutes = dict()
    for i in range(len(logs)):
        id, time = logs[i][0], logs[i][1]
        if id in user_active_minutes:
            user_active_minutes[id].add(time)
        else:
            user_active_minutes[id] = {time}

    # loop through user_active_minutes and retrieve UAM
    for id in user_active_minutes.keys():
        answer[len(user_active_minutes[id])-1] += 1
    return answer

logs = [[1,1],[2,2],[2,3]]
k = 4
print(f"Output: {findingUsersActiveMinutes(logs, k)}")